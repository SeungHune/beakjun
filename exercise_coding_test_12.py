# 스택/큐 - 주식가격

from collections import deque

def solution(prices):
    answer = []
    temp = deque(prices)
    while temp:
        price = temp.popleft()
        count = 0
        if len(temp) != 0:
            for item in temp:
                count += 1
                if price > item:
                    break
            answer.append(count)
        else:
            break
    answer.append(0)
    return answer

print(solution([1, 2, 3, 2, 3]))
print(solution([3,4,2,6,5]))