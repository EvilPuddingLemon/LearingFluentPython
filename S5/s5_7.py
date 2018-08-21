#  tag 函数用于生成HTML 标签；使用名为 cls 的关键字参数传入“class”属 性，这是一种变通方法，因为“class”是 Python 的关键字
def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s" ' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s/>' % (name, attr_str)
# 仅限关键字参数
def f(a, *, b=None):
    return a, b

if __name__ == '__main__':
    print(tag('br'))
    print('-'*20)
    print(tag('p', 'hello'))
    print('-'*20)
    print(tag('p', 'hello', 'world'))
    print('-'*20)
    print(tag('p', 'hello', id=33))
    print('-'*20)
    print(tag('p', 'hello', 'world', cls='sidebar'))
    print('-' * 20)
    print(tag(content='testing', name="img"))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'cls': 'framed'}
    print('-' * 20)
    print(tag(**my_tag))
    print('-' * 20)
    print(f(1, b=2))
    print('-' * 20)
    try:
        print(f(1, 2))
    except Exception as e:
        print('err:  ', e)