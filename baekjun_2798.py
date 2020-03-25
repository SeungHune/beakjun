#블랙잭 문제
import copy
n, m = map(int, input().split())
ans_list = []
card_list = list(map(int, input().split()))

for i in card_list:
    a_card_list = copy.deepcopy(card_list)
    a_card_list.remove(i)

    for j in a_card_list:
        b_card_list = copy.deepcopy(a_card_list)
        b_card_list.remove(j)

        for k in b_card_list:
            sum = i + j + k
            if sum <= m:
                ans_list.append(sum)

print(max(ans_list))