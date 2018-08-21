import copy


list0 = [1, 2, 3]
list1 = list0
list2 = list0.copy()
list0[0] = 0
print(list0)
print(list1)
print(list2)
list1.append(4)
print(list0)
print(list1)

list3 = [[[7, 8, 9], 5, 6], 2, 3]
list4 = list3.copy()
list5 = copy.deepcopy(list3)
list6 = copy.copy(list3)
list3[0][0][0] = 0
list3[1] = 1
print(list3)
print(list4)
print(list5)
print(list6)
list4.append(1)
print(list3)
print(list4)

class Data(object):
    def __new__(cls):
        print("new")
        cls.x = 1
        return cls
    def __init__(self):
        print("init")

data = Data()
print(data.x)

class A(object):
    def __new__(cls):
        object = super(A, cls).__new__(cls)
        print("in New")
        return object
    def __init__(self):
        print("in init")

A()

a=1
b=a
b=2
print(a)
print(b)


class PositiveInteger(int):
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))

i = PositiveInteger(-3)
print(i)


class Singleton(object):
    def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


obj1 = Singleton()
obj2 = Singleton()

obj1.attr1 = 'value1'
print (obj1.attr1, obj2.attr1)
print (obj1 is obj2)

s = u'严'



