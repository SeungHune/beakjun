n, m = map(int, input().split())
num_list = [1+_ for _ in range(n)]
# print(num_list)
check_list = [False] * n
# print(check_list)
ans_list = []

def back(cnt):
    if cnt == m:
        print(*ans_list)
        return

    for i in range(n):
        if check_list[i]:
            continue

        check_list[i] = True
        ans_list.append(num_list[i])
        # print(ans_list)

        back(cnt + 1)
        ans_list.pop()
        check_list[i] = False

back(0)