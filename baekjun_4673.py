#셀프넘버

import copy

def self_number() :
    num_list = list(map(int, range(1, 10001)))
    ans_list = copy.deepcopy(num_list)

    for i in range(len(num_list)):
        try:
            number = num_list[i]
            temp = 0

            for j in range(len(str(number))):
                a = str(number)[j]
                temp += int(a)

            non_self_number = number + temp
            ans_list.remove(non_self_number)

        except ValueError:
            pass

    for i in range(len(ans_list)):
        print(ans_list[i])

self_number()