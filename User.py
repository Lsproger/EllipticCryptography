from base.Curve import curve_P256 as p256
from Realisation.base import *
class User:
    def __init__(self, curve: Curve=p256):
        self.__curve = curve
        self.__secret_key = get_random_k(curve)
        self.__public_key = 0

    @property
    def curve(self):
        return self.__curve

    @property
    def secret_key(self):
        return self.__secret_key

    @property
    def public_key(self):
        return self.__public_key

    @public_key.setter
    def public_key(self, ):
        self.__public_key = get_public_key(self.__secret_key, self.__curve)



