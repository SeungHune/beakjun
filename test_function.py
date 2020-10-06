def solution(cacheSize, cities):
    new_cities = []
    for city in cities:
        new_cities.append(str(city).upper())
    answer = 0
    chache = [0] * cacheSize

    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for i in range(len(new_cities)):
            if new_cities[i] in chache:
                answer += 1
                temp =

            else:
                answer += 5
                for j in range(len(chache)):
                    if chache[j] == 0:
                        chache[j] = new_cities[i]
                    else:
                        chache[0] = new_cities[i]
                    print(chache)
            print("-----------")
    return answer

# print(solution(3, ["Jeju", "Pangyo", "Seoul",
#           "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))