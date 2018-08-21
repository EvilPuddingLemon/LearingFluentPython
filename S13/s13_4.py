from PythonTest.S10.s10_2 import Vector

v1 = Vector([1, 2, 3])
print(v1 * 10)
print(11 * v1)

v2 = Vector([1.0, 2.0, 3.0])
print(14 * v2)
print(v2 * True)
from fractions import Fraction
print(v2 * Fraction(1, 3))

va = Vector([1, 2, 3])
vz = Vector([5, 6, 7])
print(va @ vz == 38.0)  # 1*5+2*6+3*7
print([10, 20, 30] @ vz)
print(va @ 3)  # TypeError