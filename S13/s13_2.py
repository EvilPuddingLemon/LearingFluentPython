import decimal
ctx = decimal.getcontext()  # 获取当前全局算术运算的上下文引用
ctx.prec = 40  # 把算术运算上下文的精度设为40
one_third = decimal.Decimal('1') / decimal.Decimal('3')
print(one_third)
print(one_third == +one_third)
ctx.prec = 28  # 降低精度
print(one_third == +one_third)
print(+one_third)

from collections import Counter
ct = Counter('abracadabra')
print(ct)
ct['r'] = 3
ct['d'] = 0
print(ct)
print(+ct)




