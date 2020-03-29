# 메모리 초과,, 어찌해결하지

n = int(input())
mylist = []
m_append = mylist.append
for i in range(n):
    m_append(input())

mylist.sort()
for i in range(n):
    print(mylist[i])