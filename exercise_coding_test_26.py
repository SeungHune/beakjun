# Summer/Winter - 예산

def solution(d, budget):
    d.sort()
    answer = 0
    temp = 0
    for money in d:
        temp += money
        if temp > budget:
            break
        # print(money, temp)
        answer += 1
    return answer

print(solution([1,3,2,5,4], 9))
print(solution([2,2,2,3], 10))