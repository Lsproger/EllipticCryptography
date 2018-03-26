from User import *
from pbkdf2 import PBKDF2
import os

# Key generation
A = User()
B = User()

# A -> B

Q = B.public_key()

# Encrypting

r = get_random_k()
salt = os.urandom(8)
keylen = 256
_t_len = keylen + 128
pre_key = PBKDF2("Test ,e please!", salt).read((keylen + _t_len/8))
_t = pre_key >> keylen
K = int(bin(pre_key << _t_len)[2:keylen+2])
t = _t % curve_P256.n
print(K, t)







