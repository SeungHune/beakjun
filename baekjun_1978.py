n = int(input())
input_list = list(map(int, input().split()))
ans = 0

for i in input_list:
    check = 0
    if i != 1 :
        for j in range(2,i):
            if i % j == 0:
                check += 1
        if check == 0:
            ans += 1

print(ans)