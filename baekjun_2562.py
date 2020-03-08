mylist = []
max = 0

for i in range(9):
    mylist.append(int(input()))
    if mylist[i] > max:
        max = mylist[i]
        index = i + 1

print(max)
print(index)