n, m = map(int, input().split())
num_list = [1+_ for _ in range(n)]
check_list = [False] * n
ans_list = []
last = []

def back(cnt):
    if cnt == m:
        last.append(list(ans_list))
        print(ans_list)
        return

    for i in range(n):
        if check_list[i]:
            continue

        check_list[i] = True
        ans_list.append(num_list[i])
        back(cnt + 1)
        ans_list.pop()
        check_list[i] = False

back(0)
print(last)
for i in last:
    sorted(i)
print(last)