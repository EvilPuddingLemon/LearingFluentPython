from functools import wraps

def coroutine(func):
    """装饰器：向前执行到第一个`yield`表达式，预激`func`"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)  # 调用被装饰的函数，获取生成器对象。
        next(gen)  # 预激生成器。
        return gen  # 返回生成器
    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

if __name__ == '__main__':
    from inspect import getgeneratorstate
    coro_avg = averager()
    print(getgeneratorstate(coro_avg))
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))
