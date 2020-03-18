t = int(input())
ans_list = []

for i in range(t):
    _0_floor = []
    for i in range(14):
        _0_floor.append(i + 1)

    k = int(input()) #층
    n = int(input()) #호수
    temp = 0

    while True:
        if k <= 0:
            break
        else:
            for j in range(n):
                temp += _0_floor[j]
                _0_floor[j] = temp
            k -= 1
            temp = 0

    ans_list.append(_0_floor[n-1])

for i in ans_list:
    print(i)