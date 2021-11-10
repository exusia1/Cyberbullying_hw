from Auth import Auth

auth_config = input('Print "one-time" for one-time answer or "time" for time-based OTP: ')
server = Auth(auth_config)

while True:
    username = input('Enter your username: ')

    server.auth(username)
    if input('Print "relog" to auth again: ') != 'relog':
        break
