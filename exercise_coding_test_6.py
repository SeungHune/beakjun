# 정렬 - 가장 큰 수

def solution(numbers):
    if sum(numbers) == 0:
        return "0"
    new_numbers = []
    for num in numbers:
        new_numbers.append(str(num) * 3)

    new_numbers.sort(reverse=True)
    # print(new_numbers)
    answer = ""
    for num in new_numbers:
        if len(num) == 3:
            answer += num[0]
        elif len(num) == 6:
            answer += num[:2]
        elif len(num) == 9:
            answer += num[:3]
        else:
            answer += num[:4]

    return answer

# print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))
# print(solution([9, 303, 89, 898]))
# print(solution([112, 11, 121, 0]))
print(solution([40,404]))
print(solution([0,0,0,0]))