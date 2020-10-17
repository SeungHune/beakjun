# 해시 - 위장

def solution(clothes):
    kind = []
    for i in range(len(clothes)):
        kind.append(clothes[i][1])
    kind = list(set(kind))
    count_kind = [0 * _  + 1 for _ in range(len(kind))]
    # print(count_kind)
    for i in range(len(kind)):
        for item in clothes:
            if kind[i] in item:
                count_kind[i] += 1
    ans = 1
    for a in count_kind:
        ans = ans * a
    return ans - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
                ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"],
                ["smoky_makeup", "face"]]))
print(solution([["crow_mask", "face"], ["asd", "dss"]]))