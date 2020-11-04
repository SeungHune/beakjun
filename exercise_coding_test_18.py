# 월간 코드 챌린지 - 풍선 터뜨리기

def solution(a):
    answer = 1

    min_a = min(a)

    for _ in range(2):
        check = a[0]
        # print("check :",check)
        i = 1
        # print('i :',i)
        while min_a != check:
            # print('min_a :',min_a, 'check :',check,'a[i] :',a[i])
            if a[i] <= check:
                check = a[i]
                answer += 1
                # print("answer up!!")
            i += 1
            # print('i :',i)
        a.reverse()

    return answer

# print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))