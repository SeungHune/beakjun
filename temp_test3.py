from string import ascii_lowercase

def solution(encrypted_text, key, rotation):
    if rotation > 0:
        for i in range(rotation):
            a,b,c = encrypted_text.partition(encrypted_text[0])
            encrypted_text = c + b
            # print(a,b,c)
    elif rotation == 0:
        pass
    else:
        for i in range(abs(rotation)):
            a,b,c = encrypted_text.partition(encrypted_text[-1])
            encrypted_text = b + a
    key_list = list(ascii_lowercase)
    # print(key_list[1000])
    # print(key_list)
    print(encrypted_text)
    answer = ''
    for i in range(len(key)):
        num = key_list.index(key[i]) + 1
        temp = key_list.index(encrypted_text[i]) - num
        temp = temp % 26
        answer += key_list[temp]
        # break
    # print(num)
    return answer

# print(solution('qyyigoptvfb', 'abcdefghijk', -8))
print(solution("","",2))
# print(solution("ae",'aa',-27))