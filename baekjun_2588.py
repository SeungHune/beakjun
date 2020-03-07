a = int(input())
b = int(input())

c = b%10 #2의 1의자리
d = b//10
e = d%10 #2의 10의자리
f = d//10 #2의 100의자리

print(c*a)
print(e*a)
print(f*a)
print(c*a + e*a*10 + f*a*100)