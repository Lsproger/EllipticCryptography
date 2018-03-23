from base.Curve import curve_P256 as p256
from Realisation.base import *


class User:
    __secrets = {}
    __public_key = 0

    def __init__(self, curve: Curve=p256):
        self.__curve = curve
        self.__private_key = get_random_k(curve)

    @property
    def curve(self):
        return self.__curve

    @curve.setter
    def curve(self, curve: Curve=curve_P256):
        self.__curve = curve

    @property
    def public_key(self):
        return get_public_key(self.__private_key, self.__curve)

    @property
    def private_key(self):
        return self.__private_key

    def get_secret(self, user_name):
        return self.__secrets[user_name]

    def add_secret(self, user_name, public_key):
        from Realisation.ECDH import get_secret
        self.__secrets[user_name] = get_secret(self.__private_key, public_key, self.__curve)



