t = int(input())
ans_list = []

for i in range(t):
    h, w, n = map(int, input().split())
    yy = 0
    xx = 1

    for i in range(n):
        yy += 1
        if yy > h:
            xx += 1
            yy = 1

    if xx < 10:
        xx = "0" + str(xx)
        ans = str(yy) + str(xx)
    else:
        ans = str(yy) + str(xx)

    ans_list.append(ans)

for i in ans_list:
    print(i)