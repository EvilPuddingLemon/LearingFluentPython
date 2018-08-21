from PythonTest.S9.s9_2 import Vector2d
v1 = Vector2d(3, 4)
print(v1.x, v1.y)
try:
    v1.x = 7
except AttributeError as e:
    print(e)

try:
    print(hash(v1))
except TypeError as e:
    print(e)
try:
    print(set([v1]))
except TypeError as e:
    print(e)

v2 = Vector2d(3.1, 4.2)
print(hash(v1), hash(v2))
print(set([v1, v2]))

print(v1.__dict__)
print(v1._x)