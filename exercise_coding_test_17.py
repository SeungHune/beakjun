# 연습문제 - 가장 긴 팰린드롬

def solution(s):
    original = s
    odd_max_num = 0
    even_max_num = 0

    for i in range(len(original)):
        odd_check = True
        even_check = False
        odd_left = i
        odd_right = i
        letter_odd = original[i]
        letter_even = original[i]
        try:
            if original[i] == original[i + 1]:
                even_check = True
                even_right = odd_right + 1
                even_left = odd_left
                letter_even = original[even_left:even_right + 1]
        except IndexError:
            pass

        while odd_check:
            if odd_left > 0:
                odd_left -= 1
            if odd_right < len(original):
                odd_right += 1
            # print(left, right)
            try:
                if original[odd_left] == original[odd_right] :
                    letter_odd = original[odd_left:odd_right + 1]
                    # print('i :', i)
                    # print(letter_odd)
                    continue
                else:
                    odd_check = False
            except IndexError:
                break

        while even_check:
            if even_left > 0:
                even_left -= 1
            if even_right < len(original):
                even_right += 1
            try:
                if original[even_left] == original[even_right] :
                    letter_even = original[even_left:even_right + 1]
                    # print('i :', i)
                    # print("here")
                    # print(letter_even)
                    continue
                else:
                    even_check = False
            except IndexError:
                break

        if odd_max_num < len(letter_odd):
            odd_max_num = len(letter_odd)

        if even_max_num < len(letter_even):
            even_max_num = len(letter_even)

    answer = max(even_max_num, odd_max_num)

    return answer

print(solution("abcdcba"))
# print(solution("asdfg"))
# print(solution("abacde"))
# print(solution("abcdeffffegh"))
# print(solution("aaaa"))
# print(solution("abaabaaaaaaa"))
# print(solution("abcbaqwqabcba"))
# print(solution("abcbaqwertrewqq"))