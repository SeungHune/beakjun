mylist = []
temp_ans_list = []

for i in range(10):
    mylist.append(int(input()))
    temp = mylist[i] % 42
    temp_ans_list.append(temp)
    ans_list = list(set(temp_ans_list))

print(len(ans_list))