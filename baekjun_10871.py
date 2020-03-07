n,x = input().split()
n,x = int(n),int(x)

temp = ""
a = input()
left,space,right = a.partition(" ")

for i in range(n):
    if int(left) < x :
        temp = temp + " " + left
    left,space,right = right.partition(" ")

print(temp.lstrip())