# 월간 코드 챌린지 - 삼각 달팽이

# def solution(n):
#     index = 0
#     for i in range(n+1):
#         index += i
#     # print(index)
#     mylist = [1]
#     for i in range(n):
#         if i == 0 : continue
#         elif i == n - 1:
#             for j in range(i + 1):
#                 mylist.append(i + j + 1)
#         else:
#             mylist.append(i+1)
#             for _ in range(i):
#                 mylist.append(0)
#     # print(mylist)
#     num = mylist[-1]
#     # print(num)
#
#     while 0 in mylist:
#         check_back = True
#         check_front = True
#         for i in reversed(range(len(mylist))):
#             if mylist[i] == 0 and check_back:
#                 num += 1
#                 mylist[i] += num
#                 check_back = False
#             elif mylist[i] != 0:
#                 check_back = True
#
#         for j in range(len(mylist)):
#             if mylist[j] == 0 and check_front:
#                 num += 1
#                 mylist[j] += num
#                 check_front = False
#             elif mylist[j] != 0:
#                 check_front = True
#
#     return mylist

def solution(n):
    list = [[0] * n for _ in range(n)]
    # print(list)
    answer = []
    x, y = -1, 0
    num = 1
# 진짜 신박하네
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            list[x][y] = num
            print(list)
            num += 1

    for i in list:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer

print(solution(4))
# print(solution(5))
# print(solution(6))