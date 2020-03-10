n = int(input())
mylist = []

for i in range(n):
    mylist.append(int(input()))

mylist.sort()

for i in mylist:
    print(i)