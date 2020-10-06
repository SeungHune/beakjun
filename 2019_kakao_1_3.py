import copy

def powerset(s):
    masks = [1 << i for i in range(len(s))]
    for i in range(1 << len(s)):
        yield [ss for ss,mask in zip(s,masks) if mask & i]

def solution(relation):
    result_powerset = []
    for i in relation:
        result = []
        for power in powerset(i):
            result.append(power)
        result_powerset.append(result)
    result_powerset.pop(-1)
    temp = copy.deepcopy(result)
    # print(result)
    # print(temp[0])
    # print(temp)
    # print(result_powerset)

    for mother_group in result_powerset:
        for i in range(len(result)):
            # print("-----------")
            # print("마더그룹은 : ",mother_group[i], "리절트는 : ", result[i])
            try:
                if mother_group[i] == result[i]:
                    temp.remove(result[i])
            except ValueError : pass

    for i in range(len(temp)):
        temp[i] = set(temp[i])
    # print(temp[0][0])
    ans = copy.deepcopy(temp)
    for i in range(len(temp)):
        for j in range(len(temp)):
            try:
                if i < j and len(temp[j] - temp[i]) == len(temp[j]) - len(temp[i]) :
                    ans.remove(temp[j])
            except ValueError : pass
            # except IndexError : pass
    # print(temp)
    return len(ans)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],
                ["300","tube","computer","3"],["400","con","computer","4"],
                ["500","muzi","music","3"],["600","apeach","music","2"]]))

# for power in powerset(["100","ryan","music","2"]):
#     result.append(power)
#
# print(result)
