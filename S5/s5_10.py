# 使用 reduce 函数和一个匿名函数计算阶乘
from functools import reduce
def fact1(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

print(fact1(5))
# 使用 reduce 和 operator.mul 函数计算阶乘
from operator import mul
def fact(n):
    return reduce(mul, range(1, n+1))

print(fact(5))

# 演示使用 itemgetter 排序一个元组列表

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(3)):
    print(city)

print('-'*50)
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

# 定义一个 namedtuple，名为 metro_data（与示例 5-23 中的列表相同），演示使用 attrgetter 处理它
from collections import namedtuple

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
    for name, cc, pop, (lat, long) in metro_data]
print(metro_areas[0])
print(metro_areas[0].coord.lat)
from operator import attrgetter
name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))

import operator
a = [name for name in dir(operator) if not name.startswith('_')]
print(a)
print('-'*50)
for b in (name for name in dir(operator) if not name.startswith('_')):
    print(b, end=', ')
print('\n'+'-'*50)
# methodcaller 使用示例：第二个测试展示绑定额外参数的方式
from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))
print(s.upper())
hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))

# 使用 partial 把一个两参数函数改编成需要单参数的可调用对象
from operator import mul
from functools import partial
triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(1, 10))))

# 使用 partial 构建一个便利的 Unicode 规范化函数
import unicodedata, functools
nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(s1 == s2)
print(nfc(s1) == nfc(s2))

# 把 partial 应用到示例 5-10 中定义的 tag 函数上
from PythonTest.S5.s5_7 import tag
print(tag)
picture = partial(tag, 'img', cls='pic-frame')
print(picture('hahah', src='wumpus.jpeg'))
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)
