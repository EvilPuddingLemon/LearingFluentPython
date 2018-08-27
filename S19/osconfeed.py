from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'

def load():

    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)

from collections import abc
import keyword

class FrozenJSON:
    """
    一个只读接口，使用属性表示法访问JSON类对象
    """

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        # 在名称为 Python 关键字的属性后面加上 _
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value
        #self.__data = dict(mapping)  # 使用mapping参数构建一个字典

    def __getattr__(self, name):    # 仅当没有指定名称的属性时才调用__getattr__方法
        if hasattr(self.__data, name):
            return getattr(self.__data, name)   # 如果name是实例属性__data的属性，返回那个属性
        else:
            # return FrozenJSON.build(self.__data[name])
            return FrozenJSON(self.__data[name])
    '''
    @classmethod
    def build(cls, obj):  # 备选构造方法
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj
    '''

'''
# 构建对象的伪代码
def object_maker(the_class, some_arg):     
    new_object = the_class.__new__(some_arg)
    if isinstance(new_object, the_class):         
        the_class.__init__(new_object, some_arg)
    return new_object
'''

if __name__ == '__main__':

    feed = load()
    print(sorted(feed['Schedule'].keys()))
    for key, value in sorted(feed['Schedule'].items()):
        print('{:3} {}'.format(len(value), key))
    print(feed['Schedule']['speakers'][-1]['name'])
    print(feed['Schedule']['speakers'][-1]['serial'])
    print(feed['Schedule']['events'][40]['name'])
    print(feed['Schedule']['events'][40]['speakers'])

    print('-' * 50)
    raw_feed = load()
    feed = FrozenJSON(raw_feed)
    print(len(feed.Schedule.speakers))
    print(sorted(feed.Schedule.keys()))
    for key, value in sorted(feed.Schedule.items()):
        print('{:3} {}'.format(len(value), key))

    print(feed.Schedule.speakers[-1].name)
    talk = feed.Schedule.events[40]
    print(type(talk))
    print(talk.name)
    print(talk.speakers)
    try:
        print(talk.flavor)
    except KeyError as e:
        print('KeyError: '+str(e))
    grad = FrozenJSON({'name': 'Jim Bo', 'class': 1982})
    # print(getattr(grad, 'class'))
    print(grad.class_)
