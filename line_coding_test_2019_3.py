import copy
from itertools import combinations

def solution(road,n):
    position_0 = []
    for i in range(len(road)):
        if road[i] == "0":
            position_0.append(i)

    if len(position_0) <= n:
        return len(road)

    codmbi = list(combinations(position_0, n))

    max_dis = 0
    for i in range(len(codmbi)):
        temp_max = 0
        temp = list(map(int, road))
        for j in range(len(codmbi[i])):
            temp[j] = 1
        for i in range(len(temp)-1):
            if temp[i] == 1 and temp[i+1] == 1:
                temp_max += 1
                if temp_max > max_dis:
                    max_dis = temp_max

    return max_dis

print(solution("111011110011111011111100011111",3))
print(solution("001100", 5))