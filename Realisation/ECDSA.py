from Realisation.base import *
from Realisation.Hash import *
import random


def get_signature(z, private_key, curve: Curve=curve_P256):
    lz = len(str(z))
    ln = len(str(curve.n))
    if lz != ln:
        print('ZALUPAAAAAAAA = lz - ln = ', lz-ln)
    s = r = k = 0
    _r = lambda __k: multiply(curve.g, k).x % curve.n
    while s == 0:
        k = get_random_k()
        while r == 0:
            r = _r(k)
        _k_ = inverse_of(k, curve.n)
        what = (z + r * private_key)
        s = (_k_ * what) % curve.n
    print('r = ', r, '\n', 's = ', s)
    return r, s


def check_signature(public_key, z, signature, curve: Curve=curve_P256):
    u1 = (inverse_of(signature[1], curve.n) * z) % curve.n
    u2 = (inverse_of(signature[1], curve.n) * signature[0]) % curve.n
    u1G = multiply(curve.g, u1)
    u2Q = multiply(public_key, u2)
    P = points_sum(u1G, u2Q)
    _r = P.x % curve.n
    if signature[0] == _r:
        return 1
    else:
        return 0


def sign_message(private_key, message, curve):
    z = get_hash(message, curve.n)

    r = 0
    s = 0

    while not r or not s:
        k = random.randrange(1, curve.n)
        p = multiply(curve.g, k)

        r = p.x % curve.n
        s = ((z + r * private_key) * inverse_of(k, curve.n)) % curve.n

    return r, s


def verify_signature(public_key, message, signature, curve):
    z = get_hash(message, curve.n)

    r, s = signature

    w = inverse_of(s, curve.n)
    u1 = (z * w) % curve.n
    u2 = (r * w) % curve.n

    p = points_sum(multiply(curve.g, u1),
                   multiply(public_key, u2))

    if (r % curve.n) == (p.x % curve.n):
        return 'signature matches'
    else:
        return 'invalid signature'




