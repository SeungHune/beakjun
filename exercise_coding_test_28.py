
def solution(n):
    ans = 0
    temp = 1
    while temp*2 < n:
        temp = temp * 2
    print(temp)

    return ans

print(solution(5))
print(solution(6))