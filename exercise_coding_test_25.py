# Summer/Winter - 소수 만들기

import itertools
import math

def is_prime(num):
    # print(num)
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            # print("소수아니다")
            return False
    # print("소수다")
    return True

def solution(nums):
    answer = 0
    sub = []
    temp = itertools.combinations(nums, 3)

    for item in temp:
        # print(sum(item))
        if is_prime(sum(item)):
            # print(sum(item))
            sub.append(item)
            answer += 1

    return answer

# print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))