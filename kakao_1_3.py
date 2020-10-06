def turn_right(key):
    new_key = [[0] * len(key) for y in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            new_key[j][len(key)-1-i] = key[i][j]
    return new_key

def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_n = n*3
    new_lock = [[0] * new_n for _ in range(new_n)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    cnt = 0
    while True:
        if cnt > new_n*new_n*3 :
            return False
        sub_x = 0
        sub_y = 0
        #전체 비교하는방법........

        for i in range(new_n-m-1):
            flag = True
            for j in range(m):
                for k in range(m):
                    if key[j][k] + new_lock[j+sub_x][k+sub_y] >= 2:
                        flag = flag * False
                    elif key[j][k] + new_lock[j+sub_x][k+sub_y] == 0:
                        flag = flag * False
                    else:
                        flag = flag * True
                    sub_y += 1
                sub_y = 0
                sub_x += 1
                if flag == True:
                    return True
            cnt += 1

# print(turn_right([[0, 0, 0], [1, 0, 0], [0, 1, 1]]))
print(solution([[0, 0], [1, 0]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))