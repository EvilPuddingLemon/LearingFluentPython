from PythonTest.S10.s10_2 import Vector

v1 = Vector([3, 4, 5])
v2 = Vector([6, 7, 8])
print(v1+v2)
v3 = Vector([1, 2])
print(v1+v3)
print(v1 + (10, 20, 30))
try:
    print((10, 20, 30) + v1)
except TypeError as e:
    print(e)

print(v1 + 'ABC')