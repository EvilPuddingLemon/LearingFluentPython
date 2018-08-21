brl = 1/2.43
print(brl)
print(format(brl, '0.4f'))
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))

print(format(42, 'b'))
print(format(2/3, '.1%'))

from datetime import datetime
now = datetime.now()
print(format(now, '%H:%M:%S'))
print("It's now {:%I:%M %p}".format(now))

from PythonTest.S9.s9_2 import Vector2d
v1 = Vector2d(3, 4)
print(format(v1))
print(format(v1, '.3f'))
print(format(v1, '.3e'))
print(format(v1, 'p'))
