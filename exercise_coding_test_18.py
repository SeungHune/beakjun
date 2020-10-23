# 월간 코드 챌린지 - 풍선 터뜨리기

def solution(a):
    answer = 2

    for i in range(1,len(a)-1):
        target = a[i]
        right_min = min(a[i:])
        left_min = min(a[:i+1])

        if right_min == target or left_min == target:
            answer += 1

    return answer

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))