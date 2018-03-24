from base.Curve import curve_P256
from base.Point import Point

import collections

EllipticCurve = collections.namedtuple('EllipticCurve', 'name p a b g n h')

curve = EllipticCurve(
    'secp256k1',
    # Field characteristic.
    p=0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff,
    # Curve coefficients.
    a=-3,
    b=0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
    # Base point.
    g=(0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
       0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5),
    # Subgroup order.
    n=0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551,
    # Subgroup cofactor.
    h=1,
)


def inverse_mod(k, p):
    """Returns the inverse of k modulo p.
    This function returns the only integer x such that (x * k) % p == 1.
    k must be non-zero and p must be a prime.
    """
    if k == 0:
        raise ZeroDivisionError('division by zero')

    if k < 0:
        # k ** -1 = p - (-k) ** -1  (mod p)
        return p - inverse_mod(-k, p)

    # Extended Euclidean algorithm.
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    gcd, x, y = old_r, old_s, old_t

    assert gcd == 1
    assert (k * x) % p == 1

    return x % p


# Functions that work on curve points #########################################

def is_on_curve(point):
    """Returns True if the given point lies on the elliptic curve."""
    if point is None:
        # None represents the point at infinity.
        return True

    x, y = point

    return (y * y - x * x * x - curve.a * x - curve.b) % curve.p == 0


def point_neg(point):
    """Returns -point."""
    assert is_on_curve(point)

    if point is None:
        # -0 = 0
        return None

    x, y = point
    result = (x, -y % curve.p)

    assert is_on_curve(result)

    return result


def point_add(point1, point2):
    """Returns the result of point1 + point2 according to the group law."""
    assert is_on_curve(point1)
    assert is_on_curve(point2)

    if point1 is None:
        # 0 + point2 = point2
        return point2
    if point2 is None:
        # point1 + 0 = point1
        return point1

    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 and y1 != y2:
        # point1 + (-point1) = 0
        return None

    if x1 == x2:
        # This is the case point1 == point2.
        inv_2y = inverse_mod(2 * y1, curve.p)
        x2a = 3 * x1 * x1 + curve.a
        m = x2a * inv_2y
    else:
        # This is the case point1 != point2.
        m = (y1 - y2) * inverse_mod(x1 - x2, curve.p)

    x3 = m * m - x1 - x2
    y3 = y1 + m * (x3 - x1)
    result = (x3 % curve.p,
              -y3 % curve.p)

    assert is_on_curve(result)

    return result


# --------------------------------

def extended_euclidean_algorithm(a, b):
    """
    Возвращает кортеж из трёх элементов (gcd, x, y), такой, что
    a * x + b * y == gcd, где gcd - наибольший
    общий делитель a и b.

    В этой функции реализуется расширенный алгоритм
    Евклида и в худшем случае она выполняется O(log b).
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def inverse_of(k, p):
    """Returns the inverse of k modulo p.
    This function returns the only integer x such that (x * k) % p == 1.
    k must be non-zero and p must be a prime.
    """
    if k == 0:
        raise ZeroDivisionError('division by zero')

    if k < 0:
        # k ** -1 = p - (-k) ** -1  (mod p)
        return p - inverse_mod(-k, p)

    # Extended Euclidean algorithm.
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    gcd, x, y = old_r, old_s, old_t

    assert gcd == 1
    assert (k * x) % p == 1

    return x % p
    # """
    # Возвращает обратную величину
    # n по модулю p.
    #
    # Эта функция возвращает такое целое число m, при котором
    # (n * m) % p == 1.
    # """
    # gcd, x, y = extended_euclidean_algorithm(n, p)
    # assert (n * x + p * y) % p == gcd
    #
    # if gcd != 1:
    #     # Или n равно 0, или p не является простым.
    #     raise ValueError(
    #         '{} has no multiplicative inverse '
    #         'modulo {}'.format(n, p))
    # else:
    #     return x % p


def points_sum(p1: Point, p2: Point, a=curve.a):

    s = 0
    mod_m = curve_P256.n
    if p1.x != p2.x:
        s = ((p1.y - p2.y) * inverse_of((p1.x - p2.x), mod_m))

    else:
        if p1.y == -p2.y:
            return Point(0, 0)
        elif p1.y == p2.y and p1.y == 0:
            return Point(0, 0, 0)
        else:
            y = p1.y
            inv_2y = inverse_mod(2 * y, mod_m)
            x2a = ((3 * p1.x * p1.x) + a)
            s = (x2a * inv_2y)
    if s != 0:

            r_x = ((s * s) - p1.x - p2.x)
            r_y = (-p1.y + s * (p1.x - r_x))
    else:
        print("NE MOZHET BIT?")
    return Point(r_x % mod_m, r_y % mod_m)


res1 = point_add(curve.g, curve.g)

poent = Point(curve.g[0], curve.g[1])

res2 = points_sum(poent, poent, curve.a)


if res1[0] == res2.x and res1[1] == res2.y:
    print('PIZDEC')
else:
    print("NASHEL!!!!!")
