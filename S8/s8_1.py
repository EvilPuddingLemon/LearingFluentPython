# 变量 a 和 b 引用同一个列表，而不是那个列表的副本
a = [1, 2, 3]
b = a
a.append(4)
print(b)

# 创建对象之后才会把变量分配给对象
class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))

x = Gizmo()  #  输出的 Gizmo id: ... 是创建 Gizmo 实例的副作用
try:
    y = Gizmo() * 10  # 在乘法运算中使用 Gizmo 实例会抛出异常,而输出表明在尝试求积之前其实会创建一个新的 Gizmo 实例
except TypeError as e:
    print(e)

print(dir())  # 但是，肯定不会创建变量 y，因为在对赋值语句的右边进行求值时抛出了异常