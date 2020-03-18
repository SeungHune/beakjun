n = int(input())
weight_list = []
height_list = []
ans_list = []

for i in range(n) :
    weight, height = map(int, input().split())
    weight_list.append(weight)
    height_list.append(height)
    ans_list.append(1)

for i in range(n):
    for j in range(n):
        if weight_list[i] >= weight_list[j]:
            temp_weight_bool = True
        else:
            temp_weight_bool = False

        if height_list[i] >= height_list[j]:
            temp_height_bool = True
        else:
            temp_height_bool = False

        if temp_height_bool == False and temp_weight_bool == False:
            ans_list[i] += 1

temp = ""
for i in ans_list:
    temp = temp + " " + str(i)

print(temp.strip())
