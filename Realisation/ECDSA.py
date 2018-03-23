from Realisation.base import *


def get_signature(z, private_key, curve: Curve=curve_P256):
    s = r = k = 0
    _r = lambda __k: get_public_key(k, curve).x
    while s == 0:
        k = get_random_k()
        while r == 0:
            r = _r(k)
        s = (inverse_of(k, curve.n) * (z + r * private_key)) % curve.n
    return r, s


def check_signature(public_key, z, signature, curve: Curve):
    u1 = inverse_of((signature[1], curve.n) * z) % curve.n
    u2 = inverse_of((signature[0], curve.n) * z) % curve.n
    P = points_sum(
        multiply(curve.g, u1, curve.a),
        multiply(public_key, u2, curve.a))
    if signature[0] == P.x:
        return 1
    else:
        return 0







