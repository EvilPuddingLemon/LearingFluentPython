from PythonTest.S10.s10_2 import Vector

v1 = Vector([3, 4, 5])
print(len(v1))
print(v1[0], v1[-1])
v7 = Vector(range(7))
print(v7[1:4])

class MySeq:
    def __getitem__(self, index):
        return index

s = MySeq()
print(s[1])
print(s[1:4])
print(s[1:4:2])
print(s[1:4:2, 9])
print(s[1:4:2, 7:9])
print(slice)
print(dir(slice))
#print(help(slice.indices))
print(slice(None, 10, 2).indices(5))
print(slice(-3, None, None).indices(5))

print(v7[-1])
print(repr(v7[1:4]))
print(repr(v7[-1:]))
print(v7[1, 2])