n = int(input())
mylist = []
anslist = []

for i in range(n):
    temp_ans = 0
    point = 1
    mylist.append(input())
    length = len(mylist[i])

    for j in range(length):
        if mylist[i][j] == "O":
            if mylist[i][j-1] == "O" and j-1 != -1:
                point += 1
            else:
                point = 1
            temp_ans = temp_ans + point
    anslist.append(temp_ans)

for i in range(len(anslist)):
    print(anslist[i])