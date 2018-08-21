from PythonTest.S10.s10_2 import Vector

v = Vector(range(5))
v2 = Vector(range(6))
v3 = Vector([0, 1, 2, 3, 4])
print(repr(v))
print(v.x)
try:
    v.x = 10
except AttributeError as e:
    print(e)
print(v.x)
print(repr(v))

print(v == v2)
print(v == v3)