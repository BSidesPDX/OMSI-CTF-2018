import os
import re
import io
import time
import hashlib
import subprocess
from random import randrange
from base64 import b16encode, b64encode
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
engine = create_engine('sqlite:////data/db')
Base = declarative_base()
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
gsession = Session()
font = '/usr/share/fonts/truetype/freefont/FreeSerif.ttf'


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    captcha  = Column(String)
    session = Column(String)
    credits = Column(Integer)


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    item = Column(String)
    cost = Column(Integer)
    deliver = Column(String)

index_html = open('index.html').read()

def make_session(username):
    # bug #1: easy session forgery
    return b16encode('{"user":"%s", "valid":1}' % username)


def init_db():
    Base.metadata.create_all(bind=engine)
    gsession.query(Users).delete()
    gsession.query(Items).delete()
    gsession.commit()
    gsession.add(Users(username='admin',
                         password=b16encode(os.urandom(16)),
                         session=make_session('admin'),
                         credits=1e12))
    gsession.add(Items(item='flag',
                         cost=100000,
                         deliver='cat flag'))
    gsession.add(Items(item='fortune',
                         cost=12,
                         deliver='/usr/games/fortune'))
    gsession.add(Items(item='hint',
                         cost=101,
                         deliver='shuf -n 1 hints'))
    gsession.commit() 


def randlight():
    return (randrange(200,255), randrange(200,255), randrange(200,255))


def randfill():
    return (randrange(0,225), randrange(0,225), randrange(0,225), 255)


def reqlogin(fn):
    def wrap(*args, **kwargs):
        print(request.json)
        cuser = request.json['username']
        cpass = request.json['password']
        user = request.session.query(Users).filter(Users.username == cuser).first()
        if not user or user.password != hashpass(cpass):
            return make_response('login failed', 400)
        return fn(user)
    wrap.__name__ = fn.__name__
    return wrap


def reqsess(fn):
    def wrap(*args, **kwargs):
        sessioncookie = request.cookies.get('session')
        if sessioncookie == None:
            return make_response('requires session', 400)
        user = request.session.query(Users).filter(Users.session == sessioncookie).first()
        print('got session cookie: %s %s' % (sessioncookie, user))
        if not user:
            return make_response('invalid session', 400)
        return fn(user)
    wrap.__name__ = fn.__name__
    return wrap


def hashpass(password):
    return b16encode(hashlib.md5(password).digest())


@app.route('/')
def index():
    return index_html

@app.route('/directory')
@reqsess
def directory(user):
    ul = request.session.query(Users).order_by(Users.credits.desc()).limit(100).all()
    rv = '<h1>Top 100 Users By Credits</h1>'
    for u in ul:
        rv += '%s: %d<br>' % (u.username, u.credits)
    return rv

@app.route('/balance')
@reqsess
def balance(user):
    r = make_response('{"username":"%s","balance":%d}', user.username, user.credits)
    r.mimetype = 'applicaiton/json'
    return r

@app.route('/transfer', methods=['POST'])
@reqsess
def transfer(user):
    touser = request.json['to']
    amount = int(request.json['amount'])
    print('transfer from %s to %s: %d credits' % (
        user.username,
        touser,
        amount))
    # bug #2: allow negative transfers
    # if amount < 0:
    #    return make_response('invalid amount', 400)
    if abs(amount) > 1000:
        return make_response('amount is too high. max 1000', 400)
    if user.credits < amount:
        return make_response('insufficient funds', 400)
    recip = request.session.query(Users).filter(Users.username == touser).first()
    if recip == None:
        return make_response('user not found', 400)
    user.credits -= amount
    recip.credits += amount
    # can't end with negative balances
    if user.credits < 0 or recip.credits < 0:
        user.credits += amount
        recip.credits -= amount
        return make_response('something went wrong', 400)
    r = make_response('{"username": "%s", "balance": %d}' % (user.username, user.credits))
    r.mimetype = 'application/json'
    request.session.commit()
    time.sleep(1)
    return r

@app.route('/buy', methods=['POST'])
@reqsess
def buy(user):
    what = request.json['item']
    f = request.session.query(Items).filter(Items.item == what).first()
    if f == None:
        return make_response('item not found', 400)
    if user.credits < f.cost:
        return make_response('insufficient funds', 400)
    else:
        user.credits -= f.cost
    print ('running subprocess')
    print (f.deliver)
    result = subprocess.check_output(f.deliver, shell=True)
    result = re.sub('[^0-9a-zA-Z _\{\}]','', result)

    r = make_response('{"username": "%s", "balance": %d, "result":"%s"}' % (user.username, user.credits, result))
    r.mimetype = 'application/json'
    request.session.commit()
    return r


@app.route('/signup', methods=['POST'])
def signup():
    cuser = request.json['username']
    if re.match('^[0-9a-zA-Z]+$',cuser) == None:
        return make_response('bad username', 400)
    cpass = request.json['password']
    time.sleep(1)
    request.session.add(Users(username=cuser,
                         password=hashpass(cpass),
                         credits=100))
    request.session.commit()
    return make_response('OK', 200)


@app.route('/captcha', methods=['POST'])
@reqlogin
def captcha(user):
    user.captcha = b64encode(os.urandom(5)).replace('=','')
    img = Image.new('RGB', (300, 100), color=randlight())
    fnt = ImageFont.truetype(font, 40)
    d = ImageDraw.Draw(img)
    xloc = 0
    for x in range(len(user.captcha)):
        l = user.captcha[x]
        xloc += 20 + randrange(10, 20)
        d.text((xloc, randrange(10, 50)),
               l,
               font=fnt,
               fill=randfill())
    output = io.BytesIO()
    img.save(output, format='JPEG')
    output.seek(0)
    image = '<img src="data:image/jpeg;charset=utf-8;base64, %s">' % (
        b64encode(output.read()))

    r = make_response(image, 200)
    r.mimetype='text/html'
    request.session.commit()
    return r


@app.route('/login', methods=['POST'])
@reqlogin
def login(user): 
    captcha = request.json['captcha']
    time.sleep(5)
    if captcha != user.captcha:
        return make_response('Invalid captcha', 400)
    user.session = make_session(user.username)
    resp = make_response('{"username":"%s","balance":%d}' % (
        user.username,
        user.credits), 200)
    resp.mimetype='text/html'
    resp.set_cookie('session', user.session)
    request.session.commit()
    return resp

@app.before_request
def getsession(*args, **kwargs):
    request.session = Session()

@app.teardown_request
def putsession(*args, **kwargs):
    Session.remove()

if __name__ == '__main__':
    print('Loaded index: %d bytes' % len(index_html))
    print('Initing database...')
    init_db()
    print('Starting app...')
    app.run(threaded=True, host='0.0.0.0', port=5001)
