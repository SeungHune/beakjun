# n, m = map(int, input().split())
# board = [list(input().split()) for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# queue = []
#
# visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
#
# def init():
#     rx, ry, bx, by = 0, 0, 0, 0
#     for i in range(n):
#         for j in range(m):
#             if board[i][j] == "R":
#                 rx, ry = i, j
#             elif board[i][j] == "B":
#                 bx, by = i, j
#     queue.append((rx, ry, bx, by, 1))
#     visited[rx][ry][bx][by] = True
#
# def move(x, y, dx, dy):
#     cnt = 0
#     while board[x+dx][y+dy] != "#" and board[x][y] != "O":
#         x += dx
#         y += dy
#         cnt += 1
#     return x, y, cnt
#
# def solve():
#     init()
#     print(queue)
#     while queue:
#         rx, ry, bx, by, depth = queue.pop(0)
#         if depth > 10:
#             break
#         for i in range(4):
#             nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
#             nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
#             if board[nbx][nby] != "O":
#                 if board[]