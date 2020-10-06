def solution(genres, plays):
    kind_genres = list(set(genres))
    temp = []

    for genre in kind_genres:
        play_genre = 0
        for i in range(len(genres)):
            if genre == genres[i]:
                play_genre += plays[i]
        temp.append([genre, play_genre])

    temp.sort(key=lambda x : x[1], reverse=True)

    anslist = [[] * _ for _ in range(len(temp))]
    for i in range(len(temp)):
        for j in range(len(plays)):
            if temp[i][0] == genres[j]:
                anslist[i].append(plays[j])

    for a in anslist:
        a.sort(reverse=True)

    ans = []
    for i in range(len(anslist)):
        if len(anslist[i]) == 1:
           ans.append(plays.index(anslist[i][0]))
        else:
            cnt = 0
            print("anslist[i] : ",anslist[i])
            for j in range(len(anslist[i])):
                print(temp[i][0],genres[plays.index(anslist[i][j])])
                if temp[i][0] == genres[plays.index(anslist[i][j])]:
                    print("hit!")
                    ans.append(plays.index(anslist[i][j]))
                    cnt += 1
                else:
                    t = 0
                    while temp[i][0] != genres[plays.index(anslist[i][j])] + t:
                        print(temp[i][0], genres[plays.index(anslist[i][j])] + t)
                        t += 1
                    ans.append(plays.index((anslist[i][j])) + t)
                if cnt == 2 : break

    return temp, anslist, ans

print(solution(["classic","classic", "pop", "classic", "classic", "pop"]
               ,[500, 600, 600, 150, 800, 2500]))