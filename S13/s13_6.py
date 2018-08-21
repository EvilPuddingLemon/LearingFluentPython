from PythonTest.S10.s10_2 import Vector
v1 = Vector([1, 2, 3])
v1_alias = v1  # 复制一份
print(id(v1))
v1 += Vector([4, 5, 6])
print(v1)
print(id(v1))
print(v1_alias)
v1 *= 11  # 每次运算都是创建了新的实例
print(v1)
print(id(v1))

import itertools

from PythonTest.S11.s11_7 import Tombola, BingoCage

class AddableBingoCage(BingoCage):

    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self

if __name__ == '__main__':
    vowels = 'AEIOU'
    globe = AddableBingoCage(vowels)
    print(globe.inspect())
    print(globe.pick() in vowels)
    print(len(globe.inspect()))
    globe2 = AddableBingoCage('XYZ')
    globe3 = globe + globe2
    print(len(globe3.inspect()))
    try:
        void = globe + [10, 20]
    except TypeError as e:
        print(e)
    globe_orig = globe
    print(len(globe.inspect()))
    globe += globe2
    print(len(globe.inspect()))
    globe += ['M', 'N']
    print(len(globe.inspect()))
    print(globe is globe_orig)
    try:
        globe += 1
    except TypeError as e:
        print(e)
