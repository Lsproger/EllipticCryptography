# Example of swapping keys
# TesT algorithm
from base.Operations import multiply
from base.Curve import curve_P256
import random


d_A = random.randint(1, curve_P256[3] - 1)
d_B = random.randint(1, curve_P256[3] - 1)

q_A = multiply(curve_P256[4], d_A)
q_B = multiply(curve_P256[4], d_B)

r_A = multiply(q_B, d_A)
r_B = multiply(q_A, d_B)

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