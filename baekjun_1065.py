n = int(input())

def han_su(n):
    count = 0
    numbers = range(1,n+1)
    num_list = list(map(int,numbers))

    for i in num_list :
        if i < 100:
            count += 1

        elif i >= 100:
            temp = str(i)
            temp_d = int(temp[1]) - int(temp[0])
            test_bool = True

            for j in range(len(temp)):
                if int(temp[j]) - int(temp[j-1]) == temp_d and j-1 != -1:
                    test_bool = test_bool and True

                elif int(temp[j]) - int(temp[j-1]) != temp_d and j-1 != -1:
                    test_bool = test_bool and False

            if test_bool == True:
                count += 1

    print(count)

han_su(n)