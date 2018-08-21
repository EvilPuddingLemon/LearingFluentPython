l1 = [3, [55, 44], (7, 8, 9)]
# l2 = l1[:]
l2 = list(l1)
# 以上2种都是浅复制
print(l2)
print(l2 == l1)
print(l2 is l1)

l1.append(100)
print('l1: ', l1)
print('l2: ', l2)
l1[1].remove(55)
print('l1: ', l1)
print('l2: ', l2)
l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1: ', l1)
print('l2: ', l2)

class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))

bus1.drop('Bill')
print(bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print(bus3.passengers)

a = [10, 20]
b = [a, 30]
a.append(b)
print(a)
from copy import deepcopy
c = deepcopy(a)
print(c)
print('-'*50)
a.append(10)
# ------------
print(a[2])
print(a[2][0])
print(a[2][0][2])
print(a[2][0][2][0])
print('-'*50)
# ------------
print(c[2])
print(c[2][0])
print(c[2][0][2])
print(c[2][0][2][0])