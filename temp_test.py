import copy
def solution(new_id):
    able = ['1','2','3','4','5','6',"7","8","9","0",
            "a",'b','c','d','e','f','g','h','i','j','k','l','m',"n",'o','p','q','r','s','t','u','v','w','x','y','z',
            '-','_','.']
    temp = new_id.lower()
    for alpha in temp:
        if alpha not in able:
            temp = temp.replace(alpha,"")
    temp = list(map(str, temp))
    temp1 = copy.deepcopy(temp)
    for i in range(len(temp)):
        if temp[i] == ".":
            start = i
            end = i
            for j in range(i+1,len(temp)):
                if temp[i] == temp[j]:
                    end += 1
                else:break
            if start != end:
                for k in range(start,end):
                    temp1[k] = ""
    temp = ""
    for i in temp1:
        temp += i
    if temp[0] == ".":
        temp = temp[1:]
    try:
        if temp[-1] == ".":
            temp = temp[:-1]
    except:IndexError
    if temp == "":
        temp = "a"
    if len(temp) >= 16:
        temp = temp[0:15]
        if temp[-1] == ".":
            temp = temp[:-1]
    last = temp[-1]
    while len(temp) < 3:
        temp += last

    return temp

# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("wd"))
# print(solution(".."))
print(solution("abcdefghijklmn.p"))