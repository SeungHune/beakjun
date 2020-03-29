# 체스판 칠하는 문제 - 오답으로 나오는데 어느 부분이 문제인지 모르겠다...
# 중간에 보드만드는거 수정

n, m = map(int, input().split())
input_board = []

for i in range(n):
    input_board.append(input())

sub_board = []

for i in range(n-7):
    for j in range(m-7):
    	borad = []
    	for row in range(i, i+8):
    		borad.append(input_board[row][j:j+8])
    	sub_board.append(borad)


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
for board in sub_board:
    WB_count = 0
    BW_count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != WB_board[i][j]:
                WB_count += 1
            if board[i][j] != BW_board[i][j]:
                BW_count += 1

    if WB_count < min :
        min = WB_count
    if BW_count < min :
        min = BW_count

print(min)