n = int(input())
d = 0
temp = 1

while True:
    temp = temp + d*6
    d += 1
    if n <= temp:
        print(d)
        break