class A:
    def ping(self):
        print('ping:', self)

class B(A):
    def pong(self):
        print('pong:', self)

class C(A):
    def pong(self):
        print('PONG:', self)

class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


d = D()
d.pong()
C.pong(d)

# Method Resolution Order 方法解析顺序
print(D.__mro__)
print('-'*50)
d.ping()
print('-'*50)
d.pingpong()
print('-'*50)
print(bool.__mro__)
def print_mro(cls):
    print(','.join(c.__name__ for c in cls.__mro__))
print_mro(bool)

from PythonTest.S11.s11_5 import FrenchDeck2
print_mro(FrenchDeck2)

import io
print_mro(io.BytesIO)
print_mro(io.TextIOWrapper)

import tkinter
print_mro(tkinter.Text)

