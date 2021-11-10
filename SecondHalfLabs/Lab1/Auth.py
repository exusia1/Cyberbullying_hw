from OTP_modules import OTPDeviceAnswer, OTPDeviceTime


class Auth:
    def __init__(self, config):
        '''
        :param str: конфигурация аутентификатора
        Создание словаря с парами User->secret
        и соответствующих девайсов
        Я предполагаю что все юзеры и секретные слова известны
        '''
        self.user2secret = {'MeMeMe': 'pass', 'user': '1234'}
        self.config = config
        if config == 'one-time':
            self.generators = {x: OTPDeviceAnswer(self.user2secret[x]) for x in self.user2secret.keys()}
            self.tries = {x: 0 for x in self.user2secret.keys()}
        if config == 'time':
            self.generators = {x: OTPDeviceTime(self.user2secret[x]) for x in self.user2secret.keys()}

    def auth(self, username):
        '''
        :param username: юзернейм
        :return: 1 если аутентификация прошла успешно и 0 иначе
        '''
        check = self.user2secret.get(username)
        if check != 0:
            true_otp = self.generators[username].get_otp()
            if self.config == 'one-time':
                print(f'Push the button: {self.tries[username] + 1} times to get the needed OTP')
                self.tries[username] += 1
            # для синхронизации OTP-устройств на 'сервере' и у владельца аккаунта
            password = input('Enter the OTP: ')
            if password == true_otp:
                print('Access granted')
                return 0
            else:
                print('Wrong password or username\n')
                return 1
        else:
            print('Wrong password or username\n')
            return 1
