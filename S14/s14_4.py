import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return  # 不是必要的

if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))

    def gen_123():
        yield 1
        yield 2
        yield 3
    print(gen_123)
    print(gen_123())
    for i in gen_123():
        print(i)
    g = gen_123()
    print(next(g))
    print(next(g))
    print(next(g))
    try:
        print(next(g))
    except StopIteration as e:
        print(e)

    def gen_AB():
        print('start')
        yield 'A'
        print('continue')
        yield 'B'
        print('end.')
    for c in gen_AB():
        print('-->', c)