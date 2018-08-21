fp = open('cafe.txt', 'w', encoding='utf_8')
print(fp)
print(fp.write('café'))
fp.close()
import os
print(os.stat('cafe.txt').st_size)
fp2 = open('cafe.txt')
print(fp2)
print(fp2.encoding)
print(fp2.read())
print(open('cafe.txt', encoding='iso8859_7').read())
fp4 = open('cafe.txt', 'rb')
print(fp4)
print(fp4.read())

import sys, locale

expressions = """
    locale.getpreferredencoding()         
    type(my_file)         
    my_file.encoding         
    sys.stdout.isatty()         
    sys.stdout.encoding         
    sys.stdin.isatty() 
    sys.stdin.encoding         
    sys.stderr.isatty()         
    sys.stderr.encoding         
    sys.getdefaultencoding()         
    sys.getfilesystemencoding() 
"""

my_file = open('dummy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))