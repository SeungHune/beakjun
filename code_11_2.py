def solution(s):
    count = 0
    num = 0
    total_count = 0
    target = 0
    while target != 1:
        num += 1
        for i in range(len(s)):
            if s[i] == "0":
                count += 1
        new_s = "1" * (len(s) - count)
        total_count += count
        count = 0
        target = len(new_s)
        # print(target)
        s = str(bin(target)[2:])
        # print(s)
        # print(new_s)
        # break
    answer = [num, total_count]
    return answer

print(solution("110010101001"))