cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[:1])
cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

# 解析16进制数字对，构建二进制序列
hex = bytes.fromhex('31 4B CE A9')
print(hex)

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
print(octets)

# 使用memporyview和struct查看一个GIF图像的首部
import struct
fmt = '<3s3sHH'  # < 是小字节序，3s3s 是两个 3 字节序列，HH 是两个 16 位二进制整数。
with open('redfox.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))

imginfo = struct.unpack(fmt, header)  # 拆包memoryview对象得到元祖，包含类型版本宽度和高度
print(imginfo)

del header  # 删除引用，释放memoryview实例所占的内存
del img
