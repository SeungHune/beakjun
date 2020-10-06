def solution(phone_book):
    phone_book.sort(key = len)
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            text = phone_book[i]
            print("text : ",text)
            print(phone_book[j])
            a,b,c = phone_book[j].partition(text)
            print(a,b,c)
            if a == "":
                # print("hit")
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))