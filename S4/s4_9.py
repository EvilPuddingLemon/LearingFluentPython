import re
import os

re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"               
            " as 1729 = 1³ + 12³ = 9³ + 10³.")

text_bytes = text_str.encode('utf_8')

print('Text', repr(text_str), sep='\n  ')
print('Numbers')
print('  str  :', re_numbers_str.findall(text_str))
print('  bytes:', re_numbers_bytes.findall(text_bytes))
print('Words')
print('  str  :', re_words_str.findall(text_str))
print('  bytes:', re_words_bytes.findall(text_bytes))

# 把字符串和字节序列参数传给 listdir 函数得到的结果
print(os.listdir('.'))
print(os.listdir(b'.'))
# 使用 surrogateescape 错误处理方式
pi_name_bytes = os.listdir(b'.')[11]
pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')
print(repr(pi_name_str))
print(pi_name_str.encode('ascii', 'surrogateescape'))
