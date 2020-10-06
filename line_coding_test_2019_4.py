import copy

def solution(snapshots, transactions):
    no_dup_transactions = copy.deepcopy(transactions)
    for i in range(len(transactions)):
        target = transactions[i]
        for j in range(len(transactions)):
            compare = transactions[j]
            if i < j:
                if target == compare:
                    no_dup_transactions.remove(compare)
    temp = {}
    for i in range(len(snapshots)):
        temp[snapshots[i][0]] = int(snapshots[i][1])

    no_dup_transactions.sort(key = lambda x : x[0])
    for transaction in transactions:
        if transaction[2] not in temp :
            temp[transaction[2]] = 0
        if transaction[1] == "SAVE":
            temp[transaction[2]] += int(transaction[3])
        else:
            temp[transaction[2]] -= int(transaction[3])

    anslist = []
    for item in temp:
        mylist = [item, str(temp[item])]
        anslist.append(mylist)

    anslist.sort(key= lambda x:x[0])

    return anslist

print(solution([["ACCOUNT1","100"],["ACCOUNT2","50"],["ACCOUNT10","150"]],
                [["1","SAVE","ACCOUNT2","100"],["2","WITHDRAW","ACCOUNT1","50"],
                 ["1","SAVE","ACCOUNT2","100"],["4","SAVE","ACCOUNT3","500"],
                 ["3","WITHDRAW","ACCOUNT2","30"],]))