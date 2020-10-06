def solution(food_times, k):
    check_list = [0 * _ for _ in range(len(food_times))]
    check = k
    while k > 0:
        if sum(food_times) == 0:
            return -1
        for i in range(len(food_times)):
            if food_times[i] > 0:
                food_times[i] -= 1
                check_list[i] += 1
                stop_index = i
                k -= 1
                # print(food_times, check_list, sum(check_list),k)
                if sum(check_list) == check:
                    break
        if sum(check_list) == check:
            break


    # print("stop : ", stop_index)
    if sum(food_times[stop_index+1:]) != 0:
        # print("aaaaaaa")
        print(food_times[stop_index+1:])
        for item in food_times[stop_index+1:]:
            # print("뒤로",item)
            if item != 0:
                ans = food_times.index(item) +1
                return ans
    else:
        # print("bbbbbbbb")
        if sum(food_times) == 0:
            return -1
        for item in food_times:
            # print("앞에서부터",item)
            if item != 0:
                ans = food_times.index(item)+1
                return ans