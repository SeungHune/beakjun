# 동적계획법 - 정수 삼각형

def solution(triangle):
    dp = [triangle[0]]
    for i, semi_list in enumerate(triangle):
        if i == 0:
            continue
        temp = []
        for j, value_semi_list in enumerate(semi_list):
            if j == 0:
                temp.append(dp[i-1][0] + value_semi_list)
            elif j == len(semi_list) - 1:
                temp.append(dp[i-1][-1] + value_semi_list)
            else:
                add_thing = max(dp[i-1][j-1], dp[i-1][j])
                temp.append(add_thing + value_semi_list)
        dp.append(temp)
    answer = max(dp[-1])
    print(triangle)
    print(dp)
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

