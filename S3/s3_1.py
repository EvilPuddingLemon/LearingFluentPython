from collections import abc
my_dict = {}
print(isinstance(my_dict, abc.Mapping))

tt = (1, 2, (30, 40))
print(hash(tt))
tl = (1, 2, [30, 40])
try:
    print(hash(tl))
except TypeError as e:
    print(e)
tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)
