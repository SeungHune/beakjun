# 체스판 칠하는 문제 - 오답으로 나오는데 어느 부분이 문제인지 모르겠다...

n, m = map(int, input().split())
input_board = []

for i in range(n):
    input_board.append(input())

sub_board = []
for i in range(n):
    for j in range(m):
        # print("---------------------------------")
        for k in range(8):
            if j+8 > n or i+8 > m:
                pass
            else:
                sub_board.append(input_board[j+k][0+i:8+i])
                # print(input_board[j+k][0+i:8+i])

# print(sub_board)
# print(len(sub_board))
_8x8_board = []
temp = []

for i in range(len(sub_board)):
    temp.append(sub_board[i])
    if i%8 == 7:
        _8x8_board.append(temp)
        temp = []

print(_8x8_board)
print(len(_8x8_board))

WB_board = ['WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW']

BW_board = ['BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB',
            'BWBWBWBW',
            'WBWBWBWB']
min = 64
for i in _8x8_board:
    WB_count = 0
    BW_count = 0
    for j in range(8):
        for k in range(8):
            if i[j][k] != WB_board[j][k]:
                WB_count += 1
                # print(j,k)
            if i[j][k] != BW_board[j][k]:
                BW_count += 1

    # print(BW_count, WB_count)
    if WB_count < min :
        min = WB_count
    if BW_count < min :
        min = BW_count

print(min)

for i in _8x8_board:
    print("------------------------------------")
    for j in range(8):
        print(i[j])

# print(WB_board[0], BW_board[0])