# 완전탐색 - 카펫

def divisor(number):
    result = []
    if number == 1:
        return [[1,1]]
    for a in range(1, int(number/2) + 1):
        if number % a == 0:
            result.append([a, int(number/a)])
    return result

def solution(brown, yellow):
    yellow_division = divisor(yellow)
    # print(yellow_division)
    all_division = divisor(brown + yellow)
    # print(all_division)
    for y in yellow_division:
        for a in all_division:
            if y[0] + 2 == a[0] and y[1] + 2 == a[1]:
                answer = a

    if answer[1] > answer[0]:
        x = answer[0]
        y = answer[1]
        answer = [y, x]
    return answer

# print(solution(10, 2))
print(solution(8,1))
print(solution(24,24))