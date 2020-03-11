t = int(input())

for i in range(t):
    r,s = input().split()
    r = int(r)
    result = ""

    for j in s:
        result = result + j * r
    print(result)