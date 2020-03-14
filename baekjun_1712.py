# a,b,c = map(int, input().split())
# break_even_point = 0
# profit = 0
# price = 0
#
# while True:
#     if profit > price:
#         break
#
#     break_even_point += 1
#     profit = c * break_even_point
#     price = a + b*break_even_point
#
# print(break_even_point)

a,b,c = map(int, input().split())
break_even_point = 0

if c <= b:
    break_even_point = -1
else:
    break_even_point = a // (c-b) +1

print(break_even_point)
