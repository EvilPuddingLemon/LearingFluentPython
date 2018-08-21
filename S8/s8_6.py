import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())  # 如果是控制台会话的话{0, 1}会绑定给_变量
a_set = {2, 3, 4}
print(wref())  # 控制台会话的话则会返回{0, 1}，因为_变量仍指代它
print(wref() is None)  # 控制台会话的话则会输出False，但是随后_变量会绑定到结果值False
print(wref() is None)  # 此时就会输出None

class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r )' % self.kind

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))
print(sorted(stock.items()))
del catalog
print(sorted(stock.keys()))
# for 循环中的变量 cheese 是全局变量，除非显式删除，否则不会消失。
del cheese
print(sorted(stock.keys()))

class MyList(list):
    """list的子类，实例可以作为弱引用的目标"""

a_list = MyList(range(10))
# a_list可以作为弱引用的目标
wref_to_a_list = weakref.ref(a_list)
print(wref_to_a_list)
print(wref_to_a_list())

