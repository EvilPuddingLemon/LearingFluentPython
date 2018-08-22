def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)

from inspect import getgeneratorstate
my_coro = simple_coroutine()
print(my_coro)
print(getgeneratorstate(my_coro))
next(my_coro)
print(getgeneratorstate(my_coro))
try:
    my_coro.send(42)
except StopIteration as e:
    print("\033[31;1mStopIteration\033[0m")
print(getgeneratorstate(my_coro))
my_coro = simple_coroutine()
try:
    my_coro.send(1729)
except TypeError as e:
    print("\033[31;1m" + str(e) + "\033[0m")

# 产出两个值的协程
def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c=', c)

my_coro2 = simple_coro2(14)
print(getgeneratorstate(my_coro2))
print(next(my_coro2))
print(getgeneratorstate(my_coro2))
print(my_coro2.send(28))
try:
    my_coro2.send(99)
except StopIteration:
    print("\033[31;1mStopIteration\033[0m")

print(getgeneratorstate(my_coro2))



