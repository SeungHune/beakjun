x = int(input())
a = 1
d = 1
diagonals_index = 0 #대각선 몇번째 줄에 있는지

while True:
    diagonals_index += 1
    ex_a = a - 1
    a = a + diagonals_index*d
    if x < a:
        break

in_diagonal_index = x - ex_a #대각선 내 어디에 있는지

if diagonals_index % 2 == 1: #대각선이 홀수번째면 위로
    up = diagonals_index + 1 - in_diagonal_index
    down = in_diagonal_index

else: #대각선이 짝수번째면 아래로
    up = in_diagonal_index
    down = diagonals_index + 1 - in_diagonal_index

print(str(up)+"/"+str(down))