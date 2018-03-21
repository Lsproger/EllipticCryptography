# Tests of methods in Operations.py
from base.Operations import *
from base.Curve import *


a = -7
b = 10


print("----TEST #1---------------")
p = Point(1, 2)
q = Point(3, 4)

r = points_sum(p, q, -7)  # -3;2
print(r.x, "|||", r.y)


print("----TEST #2---------------")
p = Point(-1, 4)
q = Point(1, 2)

r = points_sum(p, q, -7)  # 1;-2
print(r.x, "|||", r.y)


print("----TEST #3---------------")
p = Point(1, 2)
q = Point(1, 2)

r = points_sum(p, q, -7)
print(r.x, "|||", r.y)


print("----TEST #1---------------")
p = Point(-1, 4)
q = Point(1, 2)

r = points_sum(p, q, -7)
print(r.x, "|||", r.y)

