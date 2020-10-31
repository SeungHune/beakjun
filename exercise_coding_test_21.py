import itertools

def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    check = [[False for col in range(n)] for row in range(n)]
    cost_check = [[0 for col in range(n)] for row in range(n)]
    for i in range(len(check)):
        for j in range(len(check)):
            if i == j:
                check[i][j] = True
    # print(check)
    # print(costs)

    for inlist in costs:
        i = inlist[0]
        j = inlist[1]
        cost = inlist[2]
        # print(i, j, cost)
        # print(check[i][j])
        if check[i][j] == False:
            # print(i, j)
            check[i][j] = True
            check[j][i] = True
            cost_check[i][j] = cost
            cost_check[j][i] = cost
            # print(check)
            # print(cost_check)
            for k in range(len(check[i])):
                if check[i][k] and check[j][k] == False :
                    # print("hit here")
                    # print(i,k,j,k)
                    check[j][k] = True
                    check[k][j] = True
                    temp_cost = cost_check[i][k] + cost_check[i][j]
                    cost_check[j][k] = temp_cost
                    cost_check[k][j] = temp_cost

    # print(check)
    # print(cost_check)
    temp = list(itertools.chain.from_iterable(cost_check))
    answer = max(temp)
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]))