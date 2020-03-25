m = int(input())
n = int(input())
input_list = []
temp_ans_list = []

for i in range(m, n+1):
    input_list.append(i)

for i in input_list:
    count = 0
    if i != 1:
        for j in range(2,i):
            if i%j == 0:
                count += 1
        if count == 0:
            temp_ans_list.append(i)

if temp_ans_list == []:
    print(-1)
else:
    print(sum(temp_ans_list))
    print(temp_ans_list[0])

