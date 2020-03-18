# 시간초과로 실패 - 어찌줄이지?

up, down, need_to_up = map(int, input().split())
day = 0
distance = 0

while True:
    day += 1
    distance = distance + up
    if distance >= need_to_up:
        break
    distance = distance - down

print(day)
