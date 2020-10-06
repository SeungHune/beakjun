r, c, t = map(int, input().split())
# board = [[int(x) for x in input().split()]for y in range(r)]
board = []

for i in range(r):
    temp = list(map(int, input().split()))
    board.append(temp)
print(board)

def dirt_spread(board):
    return