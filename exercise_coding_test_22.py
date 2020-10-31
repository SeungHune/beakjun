import math

def solution(w,h):
    # if w == h :
    #     return w * h - h
    GCD = math.gcd(w,h)
    small_w = int(w/GCD)
    small_h = int(h/GCD)
    tilt = small_h/small_w
    # print("tilt :", tilt)
    count = 0
    before = 0
    if small_w % 2 == 0:
        check = True
        small_w = int(small_w/2)
    else:
        check = False
        small_w = int(small_w/2) + 1
        # print(small_w)
    for i in range(small_w + 1):
        if i == 0: continue
        temp = tilt * i
        count += math.ceil(temp) - before
        if not check and i == small_w:
            last = math.ceil(temp) - before
            # print(last)
        before = int(temp)
    if check :
        count = count * 2
    else:
        count = count * 2 - last

    count = count * GCD
    # print(count)
    answer = w*h - count
    return answer

print(solution(8,12))
# print(solution(12,8))
# print(solution(2,3))
# print(solution(6,18))
# print(solution(18,6))
print(solution(5,7))