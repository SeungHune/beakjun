def solution(record):
    a = {}
    ans = []
    action_arr = []
    uid_arr = []
    for i in record:
        action,b,c = i.partition(" ")
        if c.find(" ") != -1:
            uid,d,name = c.partition(" ")
        else:
            uid,name = c," "
        if action == "Enter" or action == "Change":
            a[uid] = name
        action_arr.append(action)
        uid_arr.append(uid)

    for i in range(len(action_arr)):
        if action_arr[i] == "Enter":
            temp = a[uid_arr[i]] + "님이 들어왔습니다."
            ans.append(temp)
        elif action_arr[i] == "Leave":
            temp = a[uid_arr[i]] + "님이 나갔습니다."
            ans.append(temp)
        else:pass
    return ans

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))