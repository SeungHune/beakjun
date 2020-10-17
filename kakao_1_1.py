def solution(temp):
    n = int(len(temp)/2)
    mylist = []
    ans = ""
    shortest = 1001
    if len(temp) == 1:
        return 1
    for i in range(n):
        mylist.clear()
        cut_num = i + 1
        temp_n = int(len(temp)/cut_num)
        for j in range(temp_n):
            mylist.append(temp[j*cut_num : (j+1)*cut_num])
            if 0 < len(temp[(j+1)*cut_num:]) and len(temp[(j+1)*cut_num:]) < cut_num :
                mylist.append(temp[(j+1)*cut_num:])
        print(mylist)
        mylist.append(0)
        count = 1
        for i in range(len(mylist) - 1):
            if mylist[i] == mylist[i + 1]:
                count += 1
            else:
                if count > 1:
                    ans = ans + str(count) + str(mylist[i])
                    count = 1
                else:
                    ans = ans + str(mylist[i])
        print(ans)
        print(len(ans))
        if len(ans) < shortest :
            shortest = len(ans)
        ans = ""
    return shortest

print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
# print(solution("aaaaaaaaaa"))
print(solution("a"))