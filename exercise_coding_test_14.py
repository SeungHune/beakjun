# summer/winter - 스킬트리

def solution(skill, skill_trees):
    skill_list = []
    for a in skill:
        skill_list.append(a)

    count = 0
    for skill_tree in skill_trees:
        temp = []
        check = True
        for a in skill_tree:
            if a in skill_list:
                temp.append(a)

        for i in range(len(temp)):
            if temp[i] != skill_list[i]:
                check = False
                break

        if check:
            count += 1

    return count

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))