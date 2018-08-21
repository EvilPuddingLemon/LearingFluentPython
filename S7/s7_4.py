def f1(a):
    print(a)
    print(b)
try:
    f1(3)
except NameError as e:
    print(e)
b = 6
def f2(a):
    print(a)
    print(b)
    b = 9

try:
    f2(3)
except UnboundLocalError as e:
    print(e)
def f3(a):
    global b
    print(a)
    print(b)
    b = 9
f3(3)
print(b)
f3(3)
b = 30
print(b)

from dis import dis
dis(f1)
print('-'*50)
dis(f2)