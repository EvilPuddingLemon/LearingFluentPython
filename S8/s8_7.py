import copy
t1 = (1, 2, 3)
t2 = tuple(t1)
print(t2 is t1)  # t1 和 t2 绑定到同一个对象。
t3 = t1[:]
print(t3 is t1)
t4 = (1, 2, 3)
t5 = copy.deepcopy(t1)
print(t4 is t1)
# 在控制台上建立两个一样的元祖则会输出false，而执行这个则会输出True，可能是优化了不会新建副本
print(t5 is t1)
# 而使用深复制的无论是控制台和执行都没有新建副本，都是输出True
s1 = 'ABC'
s2 = 'ABC'
print(s1 is s2)