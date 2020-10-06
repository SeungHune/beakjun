def solution(words, queries):
    temp_ans = []
    for text in queries:
        cnt = 0
        for word in words:
            flag = True
            if len(text) == len(word):
                for i in range(len(text)):
                    # print("-------------------")
                    # print("i : ", text[i])
                    # print("j : ", word[i])
                    if text[i] == "?":
                        # print("i가 물음표구만")
                        pass
                    elif text[i] != "?" and text[i] == word[i]:
                        flag = flag * True
                        # print("i가 물음표가 아니고 i랑 j가 같구만")
                    elif text[i] != "?" and text[i] != word[i]:
                        # print("둘이 다르구만")
                        flag = flag * False
                        continue
                if flag:
                    # print("hit here")
                    cnt += 1
        temp_ans.append(cnt)
    return temp_ans

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))