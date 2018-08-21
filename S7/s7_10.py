'''

registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

print('running main()')
print('registry ->', registry)
f1()

'''

registry = set()  # 集合添加和删除函数的速度更快
def register(active=True): # 接受一个可选的关键字参数
    def decorate(func):  # 内部函数是真正的装饰器
        print('running register(active={0})->decorate({1})'
              .format(active, func))
        if active:  # 只有active为真时才注册func
            registry.add(func)
        else:
            registry.discard(func)   # 如果不为真且func在registry中，就删除
        return  func  # 装饰器必须返回一个函数
    return decorate # 装饰器工厂函数返回decorate

@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')

print(registry)
print(register()(f3))
print(registry)
print(register(active=False)(f2))
print(registry)

