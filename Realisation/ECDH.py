from base.Operations import *
from base.Curve import curve_P256


def get_private_key(curve: Curve=curve_P256):
    import random
    return random.randint(1, curve.n - 1)


def get_public_key(private_key, curve: Curve=curve_P256):
    return multiply(curve.g, private_key, curve.a)


def get_secret(private_key, public_key: Point, curve: Curve=curve_P256):
    return multiply(public_key, private_key, curve.a)




