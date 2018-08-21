# 使用 lambda 表达式反转拼写，然后依此给单词列表排序
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word: word[::-1]))

# 判断对象能否调用
print(abs, str, 13)
print([callable(obj) for obj in (abs, str, 13)])

# 调用 BingoCage 实例，从打乱的列表中取出一个元素
import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(bingo())
try:
    bingo()
except Exception as e:
    print(e)
print(callable(bingo))