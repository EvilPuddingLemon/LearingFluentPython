from PythonTest.S5.s5_1 import fact, factorial
print(dir(factorial))
class C: pass
obj = C()
def func(): pass
print('\n')
print(sorted(set(dir(func)) - set(dir(obj))))