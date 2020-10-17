# 해시 - 베스트앨범

def solution(genres, plays):
    identity = list(map(int, range(len(genres))))
    mylist = []

    for i in range(len(identity)):
        mylist.append([identity[i], genres[i], plays[i]])
    # print(mylist)
    isol_genres = list(set(genres))
    find_best_genre = []

    for gen in isol_genres:
        gen_count = 0
        for item in mylist:
            if item[1] == gen:
                gen_count += item[2]
        find_best_genre.append([gen, gen_count])

    # print(find_best_genre)
    find_best_genre.sort(key=lambda x: -x[1])
    # print("find_best_genre :",find_best_genre)
    mylist.sort(key=lambda x: (-x[2], x[0]))
    # print("mylist :",mylist)

    answer = []
    for i in range(len(find_best_genre)):
        genre = find_best_genre[i][0]
        control = 0
        sub_control = 0
        while(control < 1):
            if sub_control > len(mylist):
                break
            for item in mylist:
                if item[1] == genre:
                    answer.append(item[0])
                    control += 1
                    if control >= 2:
                        break
            sub_control += 1
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))