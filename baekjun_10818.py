n = int(input())
text = input()

left,space,right = text.partition(" ")
min = max = int(left)

mylist = []

for i in range(n):
    mylist.append(int(left))
    left,space,right = right.partition(" ")
    if mylist[i] < min :
        min = mylist[i]
    if mylist[i] > max :
        max = mylist[i]

print(mylist)
print(min, max)