a = int(input())
b = int(input())
c = int(input())

zero_count = 0
one_count = 0
two_count = 0
three_count = 0
four_count = 0
five_count = 0
six_count = 0
seven_count = 0
eight_count = 0
nine_count = 0

total = a*b*c
total = str(total)

for i in range(len(total)):
    if total[i] == "0":
        zero_count += 1
    elif total[i] == "1":
        one_count += 1
    elif total[i] == "2":
        two_count += 1
    elif total[i] == "3":
        three_count += 1
    elif total[i] == "4":
        four_count += 1
    elif total[i] == "5":
        five_count += 1
    elif total[i] == "6":
        six_count += 1
    elif total[i] == "7":
        seven_count += 1
    elif total[i] == "8":
        eight_count += 1
    elif total[i] == "9":
        nine_count += 1

print(zero_count)
print(one_count)
print(two_count)
print(three_count)
print(four_count)
print(five_count)
print(six_count)
print(seven_count)
print(eight_count)
print(nine_count)