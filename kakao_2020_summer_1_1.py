def solution(numbers, hand):
    ans_list = []
    numbers_ = []
    r_pos, l_pos = 12, 10
    for i in numbers:
        if i == 0:
            numbers_.append(11)
        else:numbers_.append(i)
    # print(numbers_)

    for i in range(len(numbers_)):
        if numbers_[i] == 1 or numbers_[i] == 4 or numbers_[i] == 7 :
            l_pos = numbers_[i]
            ans_list.append("L")
        elif numbers_[i] == 3 or numbers_[i] == 6 or numbers_[i] == 9 :
            r_pos = numbers_[i]
            ans_list.append("R")
        else:
            if r_pos == l_pos and hand == "left" :
                l_pos = numbers_[i]
                ans_list.append("L")
            elif r_pos == l_pos and hand == "right" :
                r_pos = numbers_[i]
                ans_list.append("R")
            l_gap = abs(l_pos - numbers_[i])
            r_gap = abs(r_pos - numbers_[i])
            l_move_cnt = l_gap//3 + l_gap%3
            r_move_cnt = r_gap//3 + r_gap%3
            if l_move_cnt < r_move_cnt :
                ans_list.append("L")
                l_pos = numbers_[i]
            elif l_move_cnt > r_move_cnt :
                ans_list.append("R")
                r_pos = numbers_[i]
            else:
                if hand == "left" :
                    l_pos = numbers_[i]
                    ans_list.append("L")
                else:
                    r_pos = numbers_[i]
                    ans_list.append("R")
    ans = ""
    for i in ans_list :
        ans = ans + str(i)
    return ans

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))