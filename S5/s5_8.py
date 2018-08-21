import bobo

@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person

# 在指定长度附近截断字符串的函数
def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()

# 提取关于函数参数的信息
print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

# 提取函数的签名 2
print('-'*30)
from inspect import signature
sig = signature(clip)
print(repr(sig))
print(str(sig))
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)

# 把 tag 函数（见示例 5-10）的签名绑定到一个参数字典上
print('-'*30)
from PythonTest.S5.s5_7 import tag
sig = signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)
print(bound_args)
for name, value in bound_args.arguments.items():
    print(name, '=', value)
del my_tag['name']
try:
    bound_args = sig.bind(**my_tag)
except Exception as e:
    print('err:  ', e)
