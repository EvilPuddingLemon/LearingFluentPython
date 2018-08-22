EXPR = 'ssss'
'''
# 简化的伪代码， 等效于委派生成器中的RESULT = yield from EXPR语句， 不支持.throw()和.close()方法
_i = iter(EXPR)
try:
    _y = next(_i)
except StopIteration as e:
    _r = e.value
else:
    while 1:
        _s = yield _y
        try:
            _y = _i.send(s)
        except StopIteration as _e:
            _r = e.value
            break
RESULT =_r
'''
import  sys
def test():
    _i = iter(EXPR)  # EXPR是任意的可迭代对象
    try:
        _y = next(_i)  # 预激子生成器并保存结果作为产出的第一个值
    except StopIteration as _e:
        _r = _e.value   # 最简单情况下的返回值
    else:
        while 1:    # 系统会阻塞，只作为调用方和子生成器之间的通道
            try:
                _s = yield _y  # 产出子生成器当前产出的元素，等待调用方发送_s中保存的值
            except GeneratorExit as _e:  # 关闭委派生成器和子生成器
                try:
                    _m = _i.close
                except AttributeError:
                    pass
                else:
                    _m()
                raise _e
            except BaseException as _e:  # 处理调用方通过.throw传入的异常
                _x = sys.exc_info()
                try:
                    _m = _i.throw
                except AttributeError:
                    raise _e
                else:  # 如果子生成器有throw方法，调用它并传入调用方发来的异常
                    try:
                        _y = _m(*_x)
                    except StopIteration as _e:
                        _r = _e.value
                        break
            else:  # 如果产出值时没有异常
                try:
                    if _s is None:
                        _y = next(_i)
                    else:
                        _y = _i.send(_s)
                except StopIteration as _e:
                    _r = _e.value
                    break
    RESULT = _r