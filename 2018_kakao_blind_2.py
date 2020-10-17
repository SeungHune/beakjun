import copy
from string import ascii_uppercase

def solution(str1, str2):
    a = str1.upper()
    b = str2.upper()
    a_list = []
    b_list = []
    capital = list(ascii_uppercase)

    for i in range(len(a) - 1):
        a_list.append(a[i] + a[i+1])
    for i in range(len(b) - 1):
        b_list.append(b[i] + b[i+1])

    temp_a = copy.deepcopy(a_list)
    temp_b = copy.deepcopy(b_list)

    for letter in a_list:
        for i in range(2):
            try:
                if letter[i] not in capital:
                    temp_a.remove(letter)
            except ValueError:
                pass

    for letter in b_list:
        for i in range(2):
            try:
                if letter[i] not in capital:
                    temp_b.remove(letter)
            except ValueError:
                pass

    a_list = temp_a
    b_list = temp_b

    temp_a = set(a_list)
    temp_b = set(b_list)
    union_ab = list(temp_a | temp_b)
    result_union_ab = copy.deepcopy(union_ab)
    inter_ab = list(temp_a & temp_b)
    result_inter_ab = copy.deepcopy(inter_ab)

    for item in union_ab:
        maximum_a = 0
        maximum_b = 0
        for item_in_a in a_list:
            if item == item_in_a:
                maximum_a += 1
        for item_in_b in b_list:
            if item == item_in_b:
                maximum_b += 1
        maximum = max(maximum_b, maximum_a)
        if maximum != 1:
            for i in range(maximum-1):
                result_union_ab.append(item)

    for item in inter_ab:
        minimum_a = 0
        minimum_b = 0
        for item_in_a in a_list:
            if item == item_in_a:
                minimum_a += 1
        for item_in_b in b_list:
            if item == item_in_b:
                minimum_b += 1
        minimum = min(minimum_a, minimum_b)
        if minimum != 1:
            for i in range(minimum-1):
                result_inter_ab.append(item)

    # print("a_list :", a_list,"b_list :",b_list)
    # print("inter_ab :",inter_ab,"union_ab :",union_ab)
    # print(result_inter_ab, result_union_ab)

    if len(result_union_ab) == 0:
        j = 1
    else:
        j = len(result_inter_ab)/len(result_union_ab)

    answer = int(j * 65536)
    return answer

# print(solution("FRANCE", "french"))
# print(solution("E=M*C^2", "e=m*c^2"))
print(solution("aa1+aa2", "AAAA12"))