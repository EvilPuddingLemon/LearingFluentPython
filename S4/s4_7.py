fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
print(sorted(fruits))

# 使用 locale.strxfrm 函数做排序键
import locale
print(locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF-8'))
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)

# 使用 pyuca.Collator.sort_key 方法
import pyuca
coll = pyuca.Collator()
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)