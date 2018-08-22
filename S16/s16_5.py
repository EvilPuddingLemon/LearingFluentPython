from PythonTest.S16.s16_4 import averager

coro_avg = averager()
print(coro_avg.send(40))
print(coro_avg.send(50))
try:
    coro_avg.send('spam')
except TypeError as e:
    print("\033[31;1m"+str(e)+"\033[0m")
try:
    coro_avg.send(60)
except StopIteration:
    print("\033[31;1mStopIteration\033[0m")

class DemoException(Exception):
    """为这次演示定义的异常类型。"""

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received:{!r}'.format(x))
    raise RuntimeError('This line should never run')

print('-'*50)
# 激活和关闭 demo_exc_handling，没有异常
exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.send(22)
exc_coro.close()
from inspect import getgeneratorstate
print(getgeneratorstate(exc_coro))

print('-'*50)
# 把 DemoException 异常传入 demo_exc_handling 不会导致协程中止
exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(DemoException)
print(getgeneratorstate(exc_coro))

print('-'*50)
# 如果无法处理传入的异常，协程会终止
exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
try:
    exc_coro.throw(ZeroDivisionError)
except ZeroDivisionError as e:
    print("\033[31;1mZeroDivisionError\033[0m")
print(getgeneratorstate(exc_coro))

# 使用 try/finally 块在协程终止时执行操作
def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')

print('-'*50)
exc_coro = demo_finally()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(DemoException)
print(getgeneratorstate(exc_coro))
exc_coro.close()
print(getgeneratorstate(exc_coro))