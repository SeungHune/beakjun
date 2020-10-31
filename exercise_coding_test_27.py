# Summer/Winter - 영어 끝말잇기

def solution(n, words):

    past_words = [words[0]]
    back = 1
    for i in range(1,len(words)):
        now_turn = i + 1
        if now_turn % n == 1:
            back += 1
        if words[i] in past_words:
            break
        elif words[i-1][-1] != words[i][0]:
            break
        past_words.append(words[i])

    if past_words == words:
        return [0,0]
    else:
        temp = now_turn % n
        if temp == 0:
            front = n
        else:
            front = temp
    # print(now_turn)
    answer = [front, back]
    return answer

# print(solution(3,['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
print(solution(5, ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage',
                   'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']))
# print(solution(2, ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']))