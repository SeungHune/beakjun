n = int(input())

for i in range(n):
    temp_list = []
    temp_sum = 0
    for j in range(len(str(i))):
        temp_list.append(j)
        temp_sum = temp_sum + int(str(i)[j])

    ans = temp_sum + i
    # print("i : ", i , "temp_list : ", temp_list, "ans : ", ans, "temp_sum : ", temp_sum)

    if ans == n:
        print(i)
        break
    if i+1 == n:
        print(0)
