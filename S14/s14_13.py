
def f1():
    x = 0
    while True:
        x += 1
        yield x

# 得到无限循环而不是生成器
def f2():
    def do_yield(n):
        yield n
    x = 0
    while True:
        x += 1
        do_yield(x)

def f3():
    def do_yield(n):
        yield n
    x = 0
    while True:
        x += 1
        yield from do_yield(x)

d = f1()
for i in d:
    print(i)
    if i > 20:
        break

from collections import abc
e = enumerate('ABC')
print(isinstance(e, abc.Iterator))
import types
print(isinstance(e, types.GeneratorType))

# 愚蠢的示例，实现斐波那契数列生成器
class Fibonacci:

    def __iter__(self):
        return FibonacciGenerator()

class FibonacciGenerator:

    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

    def __iter__(self):
        return self

# 符合python风格的斐波那契数列生成器
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
