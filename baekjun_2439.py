t = int(input())

for i in range(0,t):
    for j in range(0, t-i):
        print(" ",end="")
    for j in range(0, i+1):
        print("*",end="")
    print()