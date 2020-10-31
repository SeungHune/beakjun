# Summer/Winter - 방문 길이

def solution(dirs):
    x,y = 0,0
    temp_path = []
    for direction in dirs:
        if direction == 'U':
            dx = -1
            dy = 0
        elif direction == "D":
            dx = 1
            dy = 0
        elif direction == "L":
            dx = 0
            dy = -1
        elif direction == "R":
            dx = 0
            dy = 1
        x = x + dx
        y = y + dy
        if not (-5 <= x <= 5 and -5 <= y <= 5):
            x = x - dx
            y = y - dy
            continue
        else:

            if direction == 'L' and ("R",x, y+1) not in temp_path:
                temp_path.append((direction, x, y))
            elif direction == 'R' and ("L", x, y-1) not in temp_path:
                temp_path.append((direction, x, y))
            elif direction == "U" and ("D", x+1, y) not in temp_path:
                temp_path.append((direction, x, y))
            elif direction == "D" and ("U", x-1, y) not in temp_path:
                temp_path.append((direction, x, y))

    temp_path = list(set(temp_path))
    # print(temp_path)
    answer = len(temp_path)
    return answer

# print(solution('ULURRDLLU'))
# print(solution("LLLLRRR"))
# print(solution("RRRRRRRRLLLL"))
# print(solution('LULLLLLLU'))
print(solution('UUUUUUUUUUUUUUUUUU'))
print(solution("UD"))
print(solution("DDU"))