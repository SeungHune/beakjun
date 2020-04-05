n = int(input())
mylist = []
for i in range(n):
    mylist.append(input())


mylist = list(set(mylist))
mylist.sort()
mylist.sort(key=len)

for i in mylist:
    print(i)