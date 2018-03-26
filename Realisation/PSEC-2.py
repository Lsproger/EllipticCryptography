from User import *
from base.Point import Point
from pbkdf2 import PBKDF2


# Key generation
def G(curve: Curve=curve_P256):
    private = get_random_k()
    public = get_public_key(private, curve)
    return private, public


# Encryption
def E(public_key: Point, curve: Curve=curve_P256):
    r = get_random_k()
    keylen = 256
    _t_len = keylen + 128
    len_ = (keylen + _t_len) / 8
    pre_key = PBKDF2(str(r)).read(int(len_))
    t_ = int.from_bytes(pre_key, 'big') >> keylen
    K = int(bin(int.from_bytes(pre_key, 'big') << _t_len)[2:keylen + 2], 2)
    t = t_ % curve.n
    T = multiply(curve.g, t, curve.a)
    U = multiply(public_key, t, curve.a)
    s = r & PBKDF2(str(T.x), bytes(U.x)).read(bin(r).__len__() - 2)
    return s, T


# Decryption
def D(private_key, s, T: Point, curve: Curve=curve_P256):
    U = multiply(T, private_key)
    r = s & PBKDF2(str(T.x), bytes(U.x)).read(bin(s).__len__() - 2)
    keylen = 256
    _t_len = keylen + 128
    len_ = (keylen + _t_len) / 8
    pre_key = PBKDF2(str(r)).read(int(len_))
    t_ = int.from_bytes(pre_key, 'big') >> keylen
    K = int(bin(int.from_bytes(pre_key, 'big') << _t_len)[2:keylen + 2], 2)
    t = t_ % curve.n
    T_ = multiply(curve.g, t, curve.a)
    if T_.x == T.x and T_.y == T.y:
        return K
    else:
        return ''

