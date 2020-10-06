import copy

def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

def solution(orders, course):
    orders.sort(key=len)
    temp = []
    for item in orders:
        for i in range(len(item)):
            temp.append(item[i])

    temp = list(set(temp))
    power = list(powerset(temp))

    temp = copy.deepcopy(power)
    for sub in power:
        if len(sub) not in course:
            temp.remove(sub)

    sub_list = []
    for item in temp:
        temp_str = ""
        for i in range(len(item)):
            temp_str += item[i]
        sub_list.append(temp_str)

    how_many_list = [0 * _ for _ in range(len(sub_list))]
    for a in range(len(sub_list)):
        combo = sub_list[a]
        for custom_combo in orders:
            check_combo = [0 * _ for _ in range(len(sub_list[a]))]
            for i in range(len(combo)):
                for j in range(len(custom_combo)):
                    if custom_combo[j].find(combo[i]) != -1 :
                        check_combo[i] = 1
            if sum(check_combo) != 0:
                how_many_list[a] += 1


    a = list(zip(sub_list,how_many_list))
    print(sub_list)
    print(how_many_list)
    print(a)
    return orders


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))