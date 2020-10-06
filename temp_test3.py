def solution(info, query):
    ans = []
    question = []
    for indi in info:
        temp = []
        lan, b, c = indi.partition(" ")
        temp.append(lan)
        position ,d, e = c.partition(" ")
        temp.append(position)
        career,f,g = e.partition(" ")
        temp.append(career)
        sour_food ,h,score = g.partition(" ")
        temp.append(sour_food)
        # temp.append(score)
        a = (temp, score)
        ans.append(a)

    for sentence in query:
        temp = []
        lan, b, c = sentence.partition(" and ")
        temp.append(lan)
        position, d, e = c.partition(" and ")
        temp.append(position)
        career,f,g = e.partition(" and ")
        temp.append(career)
        sour_food,h,score = g.partition(" ")
        temp.append(sour_food)
        # temp.append(score)
        a = (temp,score)
        question.append(a)

    anslist = [0 * _ for _ in range(len(question))]

    for i in range(len(question)):
        que = question[i]
        for j in range(len(ans)):
            an = ans[j]
            if int(que[1]) <= int(an[1]):
                check = 0
                for k in range(4):
                    if que[0][k] == "-" or que[0][k] == an[0][k]:
                        check += 1
                if check == 4:
                    anslist[i] += 1
    # for i in range(len(question)):
    #     que = question[i]
    #     # print("que:", que)
    #     for j in range(len(ans)):
    #         an = ans[j]
    #         # print("--------")
    #         # print("an :", an)
    #         check = 0
    #         for k in range(4):
    #             if que[0][k] == "-" or que[0][k] == an[0][k]:
    #                 check += 1
    #         # print(check)
    #         if check == 4 and int(que[1]) <= int(an[1]):
    #             # print("que[1] :",que[1], "an[1] :",an[1])
    #             # print("hit!!")
    #             anslist[i] += 1

    # print(ans)
    # print(question)
    return anslist

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150",
                "cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100",
                "- and - and - and - 150"]))