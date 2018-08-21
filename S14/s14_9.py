def vowel(c):
    return c.lower() in 'aeiou'
print('-'*50)
print(list(filter(vowel, 'Aardvark')))

import itertools
import operator
# 演示用于过滤的生成器函数

print(list(itertools.filterfalse(vowel, 'Aardvark')))
print(list(itertools.dropwhile(vowel, 'Aaoeiraeioudvark')))
print(list(itertools.takewhile(vowel, 'Aaeiouraeioudvark')))
print(list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))))
print(list(itertools.islice('Aardvark', 5)))
print(list(itertools.islice('Aardvark', 4, 7)))
print(list(itertools.islice('Aardvark', 1, 7, 2)))

# 演示 itertools.accumulate 生成器函数
print('-'*50)
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.accumulate(sample)))
print(list(itertools.accumulate(sample, min)))
print(list(itertools.accumulate(sample, max)))

print(list(itertools.accumulate(sample, operator.mul)))
print(list(itertools.accumulate(range(1, 11), operator.mul)))

# 演示用于映射的生成器函数
print('-'*50)
print(list(enumerate('albatroz', 1)))
print(list(map(operator.mul, range(11), range(11))))
print(list(map(operator.mul, range(11), [2, 4, 8])))
print(list(map(lambda a, b: (a, b), range(11), [2, 4, 8])))
print(list(itertools.starmap(operator.mul, enumerate('albatroz', 1))))
print(list(itertools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1))))

# 演示用于合并的生成器函数
print('-'*50)
print(list(itertools.chain('ABC', range(2))))
print(list(enumerate('ABC')))
print(list(itertools.chain(enumerate('ABC'))))  # 如果只传入一个可迭代的对象，那么 chain 函数没什么用
print(list(itertools.chain.from_iterable(enumerate('ABC'))))
print(list(zip('ABC', range(5))))
print(list(zip('ABC', range(5), [10, 20, 30, 40])))
print(list(itertools.zip_longest('ABC', range(5))))
print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))

# 演示 itertools.product 生成器函数
print('-'*50)
print(list(itertools.product('ABC', range(2))))
suits = 'spades hearts diamonds clubs'.split()
print(list(itertools.product('AK', suits)))
print(list(itertools.product('ABC')))
print(list(itertools.product('ABC', repeat=3)))
rows = itertools.product('AB', range(2), repeat=2)
for row in rows:
    print(row)

# 演示 count、repeat 和 cycle 的用法
print('-'*50)
ct = itertools.count()
print(next(ct))
print(next(ct), next(ct), next(ct))
print(list(itertools.islice(itertools.count(1, .3), 3)))
cy = itertools.cycle('ABC')
print(next(cy))
print(next(cy))
print(next(cy))
print(next(cy))
print(list(itertools.islice(cy, 7)))
rp = itertools.repeat(7)
print(next(rp), next(rp))
print(list(itertools.repeat(8, 4)))
print(list(map(operator.mul, range(11), itertools.repeat(5))))

# 组合学生成器函数会从输入的各个元素中产出多个值
print('-'*50)
print(list(itertools.combinations('ABC', 2)))
print(list(itertools.combinations_with_replacement('ABC', 2)))
print(list(itertools.permutations('ABC', 2)))
print(list(itertools.product('ABC', repeat=2)))

# itertools.groupby 函数的用法
print('-'*50)
print(list(itertools.groupby('LLLLAAGGG')))
for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)
print(animals)
for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))
for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))

# itertools.tee 函数产出多个生成器，每个生成器都可以产出输入的各个元素
print('-'*50)
print(list(itertools.tee('ABC')))
g1, g2 = itertools.tee('ABC')
print(next(g1))
print(next(g2))
print(next(g2))
print(list(g1))
print(list(g2))
print(list(zip(*itertools.tee('ABC'))))