def solution(inputString):
    ans = 0
    for item in inputString:
        if item == "[" :
            # print("11111")
            a,b,c = inputString.partition(item)
            # print(a,b,c)
            # print(c.find("]"))
            if c.find("]") != -1:
                ans += 1
            else:
                return -1
        elif item == "(":
            # print("2222222222222")
            a,b,c, = inputString.partition(item)
            if c.find(")") != -1:
                ans += 1
            else:
                return -1
        elif item == "<":
            # print("33333333333")
            a,b,c = inputString.partition(item)
            if c.find(">") != -1:
                ans += 1
            else:
                return -1
        elif item == "{":
            # print("44444444444")
            a,b,c = inputString.partition(item)
            if c.find("}") != -1:
                ans += 1
            else:
                return -1
    return ans

print(solution("Hello, world!"))
print(solution("line [plus]"))
print(solution("if (Count of eggs is 4.){Buy milk.}"))
print(solution(">_<"))