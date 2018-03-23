from base.Operations import *
from base.Curve import curve_P256


def get_random_k(curve: Curve=curve_P256):
    import random
    return random.randint(2, curve.n - 1)


def get_public_key(private_key, curve: Curve=curve_P256):
    return multiply(curve.g, private_key, curve.a)
