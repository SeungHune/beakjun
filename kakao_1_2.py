def solution(p):
    if p == "":
        return p
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == "(" :
            left += 1
        else:
            right += 1
        if left == right:
            u = p[0:i+1]
            v = p[i+1:]
            # print("u : ",u)
            # print("v : ",v)
            if u[0] == "(" and u[-1] == ")":
                # print("hit")
                temp = solution(v)
                return str(u) + str(temp)
            else:
                one = "("
                two = str(solution(v))
                three = ")"
                four = u[1:-1]
                # print("four 는 : ", four)
                table = str.maketrans("()",")(")
                four = four.translate(table)
                # for i in range(len(four)):
                #     if four[i] == "(":
                #         four[i] = ")"
                #     elif four[i] == ")":
                #         four[i] = "("
                # print("이후 four 는 : ", four)
                return one + two + three + four

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))