text = input()
check_list = ["a","b","c","d",'e','f','g','h','i','j','k','l','m','n',
              'o','p','q','r','s','t','u','v','w','x','y','z']
ans_list = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
            -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,]

for i in range(len(check_list)):
    check = 0

    for j in range(len(text)):
        if check > 0:
            break

        if check_list[i] == text[j]:
            ans_list[i] = j
            check += 1

ans_str = ""
for i in ans_list:
    ans_str = ans_str +" "+ str(i)

print(ans_str.strip())