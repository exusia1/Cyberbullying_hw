from OTP_modules import OTPDeviceAnswer, OTPDeviceTime

auth_config = input('Print "one-time" if one-time answer or "time" if time-based OTP: ')
secret = input('Enter the secret word for authenticator: ')

user_device = OTPDeviceAnswer(secret)
if auth_config == 'one-time':
    user_device = OTPDeviceAnswer(secret)
elif auth_config == 'time':
    user_device = OTPDeviceTime(secret)
else:
    print('try again')
    exit(1)

push = 0
while push <= 0:
    push = int(input('Enter the number of times to push the button: '))

while True:
    for i in range(push):
        otp = user_device.get_otp()

    print(otp)

    if push == 'stop':
        break

    if auth_config == 'one-time':
        print(f'Number of times the button was pushed: {user_device.cnt}\n')
    push = int(input('Enter the number of times to push the button: '))
