# 연습문제 - 2xn 타일링

def solution(n):
    dp = [0 for i in range(60001)]
    dp[1] = 1  #n 이 1일땐 1
    dp[2] = 2  #n 이 2일떈 2
    dp[3] = 3  #n 이 3일땐 3
    #n 이 4 일땐 5..
    #이하 동일
    for i in range(4, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    answer = dp[n]
    return answer

print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))