# 완전탐색 - 소수 찾기

from itertools import permutations

def isprime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    temp = []
    for num in numbers:
        temp.append(num)

    mylist = []
    for i in range(len(numbers)):
        mylist += list(map("".join, permutations(temp, i+1)))

    mylist2 = []
    for num in mylist:
        mylist2.append(int(num))
    mylist2 = list(set(mylist2))
    # print(mylist2)

    answer = 0
    for num in mylist2:
        if isprime(int(num)) == True:
            answer += 1

    return answer

print(solution("17"))
print(solution("011"))