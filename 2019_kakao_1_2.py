def solution(n, stages):
    fail_rate_arr = []
    for i in range(n):
        challenger = 0
        no_clear = 0
        stage_num = i + 1
        for j in range(len(stages)):
            if stage_num < stages[j]:
                challenger += 1
            elif stage_num == stages[j]:
                challenger += 1
                no_clear += 1
        if challenger == 0 and no_clear == 0:
            fail_rate = 0
        else:
            fail_rate = float(no_clear/challenger)
        ind_fail_rate = (stage_num, fail_rate)
        fail_rate_arr.append(ind_fail_rate)
    # temp = sorted(fail_rate_arr, key=lambda x : (-x[1], x[0]))
    fail_rate_arr.sort(key=lambda x : (-x[1],x[0]))
    ans = [fail_rate_arr[i][0] for i in range(n)]

    return ans

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))