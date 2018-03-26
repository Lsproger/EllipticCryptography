# Tests of methods in Operations.py
from base.Operations import *
from Realisation.ECDH import *
from Realisation.ECDSA import *
import random
from User import *
import os
from pbkdf2 import PBKDF2

# ---------------------------------------------
# ALGORITHMS
# Example of swapping keys
d_A = get_random_k()
d_B = get_random_k()

q_A = get_public_key(d_A)
q_B = get_public_key(d_B)

r_A = get_secret(d_A, q_B)
r_B = get_secret(d_B, q_A)

print("Ra params:")
print("\tx = ", r_A.x)
print("\ty = ", r_A.y)

print("\nRb params:")
print("\tx = ", r_B.x)
print("\ty = ", r_B.y)

if r_A.x == r_B.x and r_A.y == r_B.y:
    print("Nice")
    print("dA & dB params:")
    print("\tdA = ", d_A)
    print("\tdB = ", d_B)
else:
    print("Not nice :(")

# -------------------------------

Alice = User()
Bruce = User()

q_A = Alice.public_key
q_B = Bruce.public_key

Alice.add_secret('Bruce', q_B)
Bruce.add_secret('Alice', q_A)

if Alice.get_secret('Bruce').x == Bruce.get_secret('Alice').x and Alice.get_secret('Bruce').y == Bruce.get_secret('Alice').y:
    print('EEEEE\nONO RABOTAET')
else:
    print('Zaz')

hmsg = get_hash(b'Hello', curve_P256.n)

sig = get_signature(hmsg, Alice.private_key, curve_P256)

res = check_signature(Alice.public_key, hmsg, sig, curve_P256)

if res:
    print('+')
else:
    print('-')


print("----------------------------------------------------------")

