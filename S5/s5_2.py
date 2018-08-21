from PythonTest.S5.s5_1 import fact, factorial
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))
def reverse(word):
    return word[::-1]
print(reversed('testing'))
print(sorted(fruits, key=reverse))
# 计算阶乘列表：map 和 filter 与列表推导比较
print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])
# 使用 reduce 和 sum 计算 0~99 之和
from functools import reduce
from operator import add
print(reduce(add, range(100)))
print(sum(range(100)))
