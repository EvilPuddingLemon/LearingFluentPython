# charles 和 lewis 指代同一个对象
charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print(id(charles), id(lewis))
lewis['balance'] = 950
print(charles)
# alex 与 charles 比较的结果是相等，但 alex 不是 charles
alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(alex == charles)
print(alex is not charles)

# 一开始，t1 和 t2 相等，但是修改 t1 中的一个可变元素后，二者不相等了
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(id(t1[-1]))  # t1[-1] 的标识没变，只是值变了
print(t1 == t2)
