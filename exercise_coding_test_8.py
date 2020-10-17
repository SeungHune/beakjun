# 완전탐색 - 모의고사

def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    supojas = [one, two, three]
    max_correct = -1
    answer = []

    for supoja in supojas:
        a = int(len(answers)/len(supoja)) + 1
        temp = supoja * a
        indi_correct = 0

        for i in range(len(answers)):
            if answers[i] == temp[i]:
                indi_correct += 1
        if indi_correct > max_correct :
            max_correct = indi_correct
            answer = [supojas.index(supoja)+1]
        elif indi_correct == max_correct:
            answer.append(supojas.index(supoja)+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))