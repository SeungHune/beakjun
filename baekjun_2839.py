n = int(input())
number_of_bag = 0
# big_bag = 0
# small_bag = 0

while True:
    if n == 0:
        print(number_of_bag)
        break
    elif n < 0:
        print(-1)
        break
    elif n%5 != 0:
        n = n - 3
        number_of_bag += 1
        # small_bag += 1
    elif n%3 != 0:
        n = n - 5
        number_of_bag += 1
        # big_bag += 1
    elif n%5 == 0:
        a = n/5
        n = 0
        number_of_bag = number_of_bag + int(a)
        # big_bag += int(a)
    else:
        print("무슨경우냐")
        break

# print(big_bag, small_bag)