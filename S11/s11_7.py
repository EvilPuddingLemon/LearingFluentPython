import abc
import random

class Tombola(abc.ABC):

    @abc.abstractmethod  # 抽象方法
    def load(self, iterable):
        """从可迭代对象中添加元素。"""

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回
        如果实例为空，这个方法应该抛出‘LookupError'
        """

    def loaded(self):
        """如果至少有一个圆素，返回’True‘，否则返回’False‘."""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元祖，由当前元素构成"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))

class BingoCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()

class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)  # 将参数构建成列表

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))

from random import randrange

@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))



if __name__ == '__main__':
    class Fake(Tombola):
        def pick(self):
            return 13

    print(Fake)
    try:
        f = Fake()
    except TypeError as e:
        print(e)
    print(issubclass(TomboList, Tombola))
    t = TomboList(range(100))
    print(isinstance(t, Tombola))
    print(TomboList.__mro__)   # Tombolist 没有从 Tombola 中继承任何方法
