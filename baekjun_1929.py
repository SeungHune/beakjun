#에라터스테네스의 체
#시간초과.........

import math

m, n = map(int, input().split())
input_list = []
prime_list = []

for i in range(m, n+1):
    input_list.append(i)

sqrt = int(math.sqrt(n))

for i in range(n):
    count = 0
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                count += 1
        if count == 0 and i <= sqrt:
            prime_list.append(i)

for i in prime_list:
    for j in range(int(n/2)+1):
        try:
            if j > 1 :
                input_list.remove(i*j)
        except: ValueError

for i in input_list:
    print(i)