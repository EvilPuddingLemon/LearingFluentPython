city = 'São Paulo'
print(city.encode('utf_8'))
print(city.encode('utf_16'))
print(city.encode('iso8859_1'))
try:
    print(city.encode('cp437'))
except UnicodeEncodeError as e:
    print(e)
print(city.encode('cp437', errors='ignore'))
print(city.encode('cp437', errors='replace'))
print(city.encode('cp437', errors='xmlcharrefreplace'))

# 把字节序列解码成字符串：成功和错误处理
octets = b'Montr\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
print(octets.decode('koi8_r'))
try:
    print(octets.decode('utf_8'))
except UnicodeDecodeError as e:
    print(e)
print(octets.decode('utf_8', errors='replace'))

import urllib.request
import chardet
url = 'http://www.baidu.com'

a = urllib.request.urlopen(url)

'''
chardet模块
使用该模块可以查看字符串的编码格式：chardet.detect()
'''
encode = chardet.detect(a.read())
print(encode['encoding'])

#假设存在一个a.txt的文件
f = open('redfox.gif', 'rb')
print(chardet.detect(f.read(100)))

u16 = 'El Niño'.encode('utf_16')
print(u16)
print(list(u16))
u16le = 'El Niño'.encode('utf_16le')
print(u16le)
print(list(u16le))
u16be = 'El Niño'.encode('utf_16be')
print(u16be)
print(list(u16be))
