l = [1, 2, 3]
print(l*5)  # 产生新的序列
print(5*'abcd')

board = [['_'] * 3 for i in range(3)]
print(board)
board[1][2]='X'
print(board)

# 错误示范，列表内的3引用只想同一个对象
weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = '0'
print(weird_board)

# 错误，追加的是同一个对象
row = ['_'] * 3
board2 = []
for i in range(3):
    board2.append(row)
print(board2)
board2[2][0] = 'X'
print(board2)

# 正确示范
board2 = []
for i in range(3):
    row2 = ['_'] * 3
    board2.append(row2)
print(board2)
board2[2][0] = 'X'
print(board2)
