text = input()
mylist = []

for i in text:
    if i == "A"or i=="B" or i=="C":
        mylist.append(2)
    elif i == "D"or i=="E"or i=="F":
        mylist.append(3)
    elif i == "G" or i=="H" or i=="I":
        mylist.append(4)
    elif i == "J" or i=="K" or i=="L":
        mylist.append(5)
    elif i == "M" or i=="N" or i=="O":
        mylist.append(6)
    elif i == "P" or i=="Q" or i=="R" or i=="S":
        mylist.append(7)
    elif i == "T" or i=="U" or i=="V":
        mylist.append(8)
    elif i == "W" or i=="X" or i=="Y" or i=="Z":
        mylist.append(9)

ans = 0
for i in mylist:
    ans = ans + i + 1

print(ans)