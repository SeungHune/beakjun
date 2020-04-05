# 시간초과
n = int(input())
mylist = []
for i in range(n):
    mylist.append(input())

ans = sorted(mylist)

for i in range(n):
    if i+1 < n:
        age, name = ans[i].split()
        age2, no = ans[i+1].split()
        if age == age2:
            i_index = mylist.index(ans[i])
            ii_index = mylist.index(ans[i+1])
            if i_index > ii_index:
                temp = ans[i]
                ans[i] = ans[i+1]
                ans[i+1] = temp
            else:
                pass

for i in ans:
    print(i)