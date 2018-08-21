import itertools

class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> 无穷数列

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index

# 生成器函数
def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index

# 作用相同，但不是生成器函数，但会返回一个生成器，是生成器工厂函数
def aritprog_gen2(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
        return ap_gen



if __name__ == '__main__':
    ap = ArithmeticProgression(0, 1, 3)
    print(list(ap))
    ap = ArithmeticProgression(1, .5, 3)
    print(list(ap))
    ap = ArithmeticProgression(0, 1/3, 1)
    print(list(ap))
    from fractions import Fraction
    ap = ArithmeticProgression(0, Fraction(1, 3), 1)
    print(list(ap))


    gen = itertools.count(1, .5)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))

    gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
    print(list(gen))