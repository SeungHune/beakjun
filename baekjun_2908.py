#뒤집는 내장함수 알아두기

a,b = input().split()
sangsu_a = int(''.join(reversed(a)))
sangsu_b = int(''.join(reversed(b)))
mylist = [sangsu_a,sangsu_b]
mylist.sort()
print(mylist[1])
