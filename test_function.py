def solution(n, delivery):
    delivery.sort(reverse= True, key=lambda x:x[2])
    # print(delivery)
    mylist = ["?"] * n
    # print(mylist)
    for dv in delivery:
        if dv[2] == 1:
            mylist[dv[0]-1] = "O"
            mylist[dv[1]-1] = "O"
        elif dv[2] == 0:
            if mylist[dv[0]-1] == "O":
                mylist[dv[1]-1] = "X"
            elif mylist[dv[0]-1] == "X":
                mylist[dv[1]-1] = "?"
            elif mylist[dv[1]-1] == "O":
                mylist[dv[0]-1] = "X"
            elif mylist[dv[1]-1] == "X":
                mylist[dv[0]-1] = "?"

    # print(mylist)
    answer = ''
    for a in mylist:
        answer += a
    return answer

# print(solution(6,[[1,3,1],[3,5,0],[5,4,0],[2,5,0]]))
print(solution(7,[[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]))