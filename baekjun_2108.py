# 런타임 에러

import numpy as np
from collections import Counter

n = int(input())
mylist = []

for i in range(n):
    mylist.append(int(input()))

mylist.sort()
avg = int(round(np.mean(mylist),0))
mid = int(np.median(mylist))
cnt = Counter(mylist).most_common()
max_min = mylist[-1] - mylist[0]

if len(cnt) > 1 and cnt[0][1] == cnt[1][1] :
    min_ind = cnt[1][0]
else:
    min_ind = cnt[0][0]

print(avg)
print(mid)
print(min_ind)
print(max_min)