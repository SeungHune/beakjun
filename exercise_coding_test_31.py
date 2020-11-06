# 동적계획법 - 등굣길

def solution(m, n, puddles):
    dp = [[1 for col in range(m)] for row in range(n)]
    for puddle in puddles:
        x = puddle[1]-1
        y = puddle[0]-1
        dp[x][y] = 0
        if x == 0:
            for i in range(y,m):
                dp[x][i] = 0
        if y == 0:
            for i in range(x,n):
                dp[i][y] = 0

    # print(dp)
    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] != 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # print(dp)
    answer = dp[n-1][m-1] % 1000000007
    return answer

print(solution(4,3,[[2, 2]]))