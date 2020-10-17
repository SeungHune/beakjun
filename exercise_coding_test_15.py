# 124 나라의 숫자
def solution(n):
    answer = ''
    a,b = divmod(n,3)
    # print(a,b)
    if n > 3 :
        while True:
            if b == 0 :
                a -= 1
            answer = str(b) + answer
            if a == 0:
                break
            if a < 3 :
                answer = str(a) + answer
                break
            a, b = divmod(a, 3)
        # print("answer :", answer)
    elif n == 3:
        answer = "4"
    else:
        answer = str(n%3)

    # print(a,b)
    # print(answer)
    temp = ""
    for i in answer:
        if i == "1":
            temp += "1"
        elif i == "2":
            temp += "2"
        else:
            temp += "4"

    return temp