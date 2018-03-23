from base.Curve import *
from base.EuclidianAlgorithm import *


__a = curve_P256.a


def multiply(p: Point, k, a=__a):
    res = p
    _k = bin(k)[3:]  # int in bin like '0b1....'
    for n in _k:    # so we don't need 3 first bits
        if int(n):
            res = points_sum(p, points_sum(res, res, a), a)
        else:
            res = points_sum(res, res, a)
    return res


def points_sum(p1: Point, p2: Point, a=__a):

    s = 0
    mod_m = curve_P256.n
    if p1.x != p2.x:
        s = ((p1.y - p2.y) * inverse_of((p1.x - p2.x), mod_m)) % mod_m

    else:
        if p1.y == -p2.y:
            return Point(0, 0)
        elif p1.y == p2.y and p1.y == 0:
            return Point(0, 0, 0)
        else:
            s = (((3 * p1.x * p1.x) + a) * inverse_of((2 * p1.y), mod_m)) % mod_m
    if s != 0:

            r_x = ((s * s) - p1.x - p2.x) % mod_m
            r_y = (-p1.y + s * (p1.x - r_x)) % mod_m
    else:
        print("NE MOZHET BIT?")
    return Point(r_x, r_y)



# 21 * P = 10101 * P = (((((2 * P) * 2) + P) * 2) * 2 + P)


