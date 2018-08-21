import weakref
s1 = {1, 2, 3}
s2 = s1
def bye():
    print('Gone with the wind...')

ender = weakref.finalize(s1, bye) # 在 s1 引用的对象上注册 bye 回调。
print(ender.alive)
del s1  # del 不删除对象，而是删除对象的引用。
print(ender.alive)
''' 
重新绑定最后一个引用 s2，让 {1, 2, 3} 无法获取。
对象被销毁了，调用了 bye 回调， 
ender.alive 的值变成了 False。
'''
s2 = 'spam'

print(ender.alive)