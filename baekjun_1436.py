n = int(input())

ans_list = []
essential = "666"
start = 0
check_point = 0

while True:
    if len(ans_list) >= n:
        break
    start += 1000
    for i in range(check_point, start):
        if essential in str(i):
            ans_list.append(i)
    check_point = start

print(ans_list[n-1])