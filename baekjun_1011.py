## 미완성

t = int(input())
ans_list = []

for i in range(t):
    x, y = list(map(int, input().split()))
    reduce_point = int(y/2)
    speed = 0
    back_speed = 0
    distance = 0
    back_distance = 0
    up_count = 0
    down_count = 0

    while True:
        speed += 1
        distance += speed
        if x < distance:
            up_count += 1
        if distance >= reduce_point:
            break

    print(distance)
    reduce_speed_range = y - distance
    while True:
        back_speed += 1
        back_distance += back_speed
        if back_speed + back_distance >= y - distance:
            down_count += 2
            break
        if y - back_distance >= x:
            down_count += 1
        if y - back_distance == distance:
            break

    print("up_count : ", up_count, "down_count : ", down_count)
    ans_list.append(up_count + down_count)

for i in ans_list:
    print(i)