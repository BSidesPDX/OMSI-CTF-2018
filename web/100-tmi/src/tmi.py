import re
import time
from flask import Flask, request, make_response
app = Flask(__name__)

index_html = open('index.html').read()
flag = open('flag').read()
password = open('password').read().strip()
regex = '^[a-z_]+$'
if re.match(regex, password) == None:
    raise Exception('missing password file or bad password, lower and _ only')
if len(password) < 12:
    raise Exception('password file is too short. >12 char required')

def check_login(cuser, cpass):
    valid = False
    reasons = []
    if cuser != 'admin':
        reasons.append('Username is incorrect.')
    if re.match(regex, cpass) is None:
        reasons.append('Password can only conatin a-z and _,'
                       ' and must be at least 12 chars')
    for i in range(len(cpass)):
        if cpass[i] != password[i]:
            reasons.append('Password did not match, i=%d' % i)
            break
    if len(cpass) < len(password):
        reasons.append('Password too short to check all characters.')
    if len(reasons) != 0:
        return {'valid': False,
                'reason': '<BR>'.join(reasons)}
    return {'valid': True, 'reason': None}

@app.route('/')
def index():
    return index_html

@app.route('/login', methods=['POST'])
def login():
    cuser = request.form['username']
    cpass = request.form['password']
    debug = (request.form['debug'] == 'TRUE')
    # eliminate timing side channels by making sure password
    # checks take constant time of at least 1 ms (do not use IRL)
    start = time.time()
    result = check_login(cuser, cpass)
    duration = time.time()-start
    remains = 0.001 - duration
    if remains > 0:
        time.sleep(remains)
    if not result['valid']:
        if not debug:
            return make_response('Login incorrect, and not in debug mode', 400)
        else:
            return make_response(
                'check_login failed because:<BR>%s' % result['reason'], 400)
    else:
        return make_response('Login success! The flag is: %s' % flag, 200)

if __name__ == '__main__':
    print('Loaded index: %d bytes' % len(index_html))
    print('Loaded flag: %d byets' % len(flag))
    app.run(threaded=True, host='0.0.0.0')
