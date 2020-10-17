import ast
import copy

def solution(s):
    answer = []
    temp = s.replace("{", "[")
    temp = temp.replace("}", "]")
    list = ast.literal_eval(temp)
    list.sort(key=len)

    for item in list:
        if len(item) == 1:
            answer.append(item[0])
        else:
            target = copy.deepcopy(item)
            compare = copy.deepcopy(answer)
            for i in range(len(compare)):
                if compare[i] in target:
                    target.remove(compare[i])
            answer.append(target[0])

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2},{1,2},{1,2,3,4}}"))