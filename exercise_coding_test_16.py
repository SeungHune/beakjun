from collections import deque

def bfs(begin, target, words, check):
    que = deque([begin])
    result = []
    letters = []
    for word in words:
        for alphabet in word:
            letters.append(alphabet)
    letters = list(set(letters))
    letters.sort()
    print(letters)

    while que:
        word = que.popleft()
        print(word)
        result.append(word)
        for i in range(len(word)):
            new = ""
            if word[i] != target[i]:
                for j in letters:
                    print('j-',j)
                    # new = word.replace(word[i], j)
                    new = word[:i]+j+word[i+1:]
                    print('word[:i] :',word[:i],'j :',j,'word[i+1:] :', word[i+1:])
                    print(new)
                    if new not in words or check[new]:
                        continue
                    print(new,"!!")
                    break
            if new != word and new in words:
                print('hit!~!~!~')
                break
        word = new
        print("word :",word)
        if word != target and check[word] == False:
            que.append(word)
            check[word] = True
            print('여기왔냐')
        elif word == target:
            result.append(word)
    return result

def solution(begin, target, words):
    if target not in words:
        return 0
    check = {}
    for word in words:
        check[word] = False
    print(check)
    result = bfs(begin, target, words, check)
    print(result)
    answer = len(result) - 1
    return answer

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', "cog"]))
# print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))
# print(solution('hit', 'hhh',['hhh','hht']))
# print(solution('aaa', 'ccc', ['aab', 'aca', 'acb', 'abb', 'acc', 'bcc', 'ccc']))