from itertools import product

def solution(user_id, banned_id):
    result_list = []
    for ban_id in banned_id:
        candidate_list = []
        for user in user_id:
            if len(ban_id) == len(user):
                candidate_list.append(user)
        # print("candidate_list :",candidate_list)
        # print(len(ban_id),"---",ban_id)
        temp = []
        for candidate in candidate_list:
            # print("candidate :", candidate)
            for i in range(len(ban_id)):
                if ban_id[i] != "*" and ban_id[i] != candidate[i]:
                    if candidate not in temp:
                        temp.append(candidate)
                        # print("hit here")
                    continue

        for a in temp:
            candidate_list.remove(a)
        # print('new candidate_list :',candidate_list)
        result_list.append(candidate_list)
        # print("result_list :",result_list)

    result_pro = list(product(*result_list))
    last = set([frozenset(a) for a in result_pro if len(frozenset(a)) == len(banned_id)])
    # print(last)
    # print(len(last))
    return len(last)

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
print(solution(["a", "b", "c"],["a", "*"]))