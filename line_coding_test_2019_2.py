def solution(answer_sheet, sheets):
    anslist = []
    max_continuous = -1
    for i in range(len(sheets)):
        target = sheets[i]
        for j in range(len(sheets)):
            compare = sheets[j]
            count = 0
            continuous = 0
            if i < j :
                for k in range(len(answer_sheet)):
                    if target[k] == compare[k] and target[k] != answer_sheet[k]:
                        count += 1
                        continuous += 1
                        if max_continuous < continuous:
                            max_continuous = continuous
                    if target[k] != compare[k] or target[k] == answer_sheet[k]:
                        # print("hit")
                        continuous = 0
                # print("------------")
                # print("i 번 :",i+1,"j 번 :",j+1,"오답의 수는 :",count,"최대 연속오답은 :",max_continuous)
            if max_continuous == -1:
                max_continuous = 0
            anslist.append(count + max_continuous*max_continuous)
    return max(anslist)

print(solution("4132315142", ["3241523133","4121314445","3243523133",
                              "4433325251","2412313253"]))
print(solution("53241",["53241", "42133", "53241", "14354"]))
print(solution("24551", ["24553", "24553", "24553", "24553"]))