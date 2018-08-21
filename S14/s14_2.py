s = 'ABC'
for char in s:
    print(char)
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it    # 释放对it的引用，废弃迭代器对象
        break

from PythonTest.S14.s14_1 import Sentence
s3 = Sentence('Pig and Pepper')
it = iter(s3)
print(it)
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration as e:
    print(e)
print(list(it))
del it
print(list(iter(s3)))
