n = int(input())
text = input()
left,space,rigth = text.partition(" ")
mylist = []

for i in range(n):
    mylist.append(int(left))
    left,space,rigth = rigth.partition(" ")

max = max(mylist)

for i in range(n):
    mylist[i] = mylist[i]/max*100

ans = sum(mylist)/n
print(ans)