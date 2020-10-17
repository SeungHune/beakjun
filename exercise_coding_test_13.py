# 스택/큐 - 프린터

from collections import deque

def solution(priorities, location):
    temp = []
    for t in enumerate(priorities):
        temp.append(t)
    myque = deque(temp)
    count = 0
    before = len(myque)
    while True:
        target = myque.popleft()
        for item in myque:
            if target[1] < item[1]:
                myque.append(target)
                break
            else:
                pass
        after = len(myque)
        if before != after:
            count += 1
        before = after
        if target[0] == location and target not in myque:
            break

    return count

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))