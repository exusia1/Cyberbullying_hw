from hashlib import sha256
from time import time
import hmac


class OTPDeviceAnswer:
    def __init__(self, some_user_special_string):
        '''
        :param some_user_special_string: какая-то строка,
        которая уникальна для каждого пользователя и генерируется
        при получении аккауна/OTP-девайса, в случае этой лабы
        я предполагаю что она известа для каждого пользователя
        '''
        self.otp = sha256(repr(some_user_special_string).encode('utf-8')).hexdigest()
        self.cnt = 0

    def get_otp(self):
        '''
        Генерирует OTP по прошлому OTP
        '''
        to_ret = self.otp
        self.otp = sha256(repr(self.otp).encode('utf-8')).hexdigest()
        self.cnt += 1
        return to_ret


class OTPDeviceTime:
    def __init__(self, secret, interval=60):
        '''
        :param secret: секретное слово
        :param interval: интервал обновления OTP
        '''
        self.secret = secret
        self.interval = interval

    def get_otp(self):
        '''
        :return: уникальный для секретного слова,
        меняющийся каждую минуту код
        '''
        now = time() // self.interval
        return hmac.new(repr(self.secret).encode('utf-8'), repr(now).encode('utf-8'), sha256).hexdigest()
