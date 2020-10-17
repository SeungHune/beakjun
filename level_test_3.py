import copy

def solution(people, limit):
    people.sort(reverse=True)
    check = [0] * len(people)
    answer = 0
    # print(people)
    new_limit = copy.deepcopy(limit)

    for i in range(len(people)):
        # print("dodo")
        if check[i] == 0 and i != len(people) - 1:
            limit -= people[i]
            check[i] = 1

            for j in range(len(people)):
                if i < j:
                    # print("i :",i,"j :",j)
                    if check[j] == 0:
                        # print("hit here?")
                        if people[j] <= limit:
                            limit -= people[j]
                            check[j] = 1
                            # print("this?")
                            # print(check)
                            if limit == 0:
                                answer += 1
                                limit = new_limit
                        else:
                            limit = new_limit
                            answer += 1
                            # print(limit)
                            # print(answer,"개 출발")
                            # print(check)
                            break
    # print(check)
    if 0 in check:
        # print("sdf")
        answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([3,2,2,3,4,1,2,], 6))