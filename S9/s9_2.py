from array import array
import math

class Vector2d:
    #__slots__ = ('__x', '__y')
    typecode = 'd'

    def __init__(self, x, y):
        '''
        使用两个前导下划线（尾部没有下划线，或者有一个下划线），把属性标记为私有的
        '''
        self.__x = float(x)
        self.__y = float(y)

    @property  # 把读值方法标记为特性
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(self, octets):
        print(self)
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        print(memv)
        print(memv.tobytes())
        print(memv.tolist())
        print(*memv)
        print(memv[0], memv[1])
        return self(*memv)
    '''
    def __format__(self, format_spec=''):
        components = (format(c, format_spec) for c in self)
        return '({}, {})'.format(*components)
    '''
    def __format__(self, format_spec):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)


    def angle(self):
        return math.atan2(self.y, self.x)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)



if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    x, y = v1
    print(x, y)
    print(repr(v1))
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    print(v1)
    octets = bytes(v1)
    print(octets)
    print(abs(v1))
    print(bool(v1), bool(Vector2d(0, 0)))
    print(v1.frombytes(octets))
