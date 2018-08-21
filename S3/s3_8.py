l = ['spam', 'spam', 'eggs', 'span']
print(set(l))
print(list(set(l)))
haystack = {'pp1@pp', 'pp2@pp', 'pp3@pp', 'pp4@pp', 'pp5@pp', 'pp6@pp', 'pp7@pp'}
needles = {'pp1@pp', 'pp4@pp', 'pp6@pp', 'pp9@pp'}
found = len(needles & haystack)
print(found)
'''
很low的写法, 不过可以用在任何可迭代对象needles和haystack上
'''
found = 0
for n in needles:
    if n in haystack:
        found += 1

print(found)

s = {1}
print(type(s))
print(s)
s.pop()
print(s)

from dis import dis
print(dis('{1}'))
print(dis('set([1])'))

print(frozenset(range(10)))

from unicodedata import name
setcomps = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(setcomps)
