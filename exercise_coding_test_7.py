# 정렬 - H-Index

def solution(citations):
    max_num = max(citations)
    max_count = -1

    if sum(citations) == 0:
        return 0

    for cita in range(1, max_num + 1):
        count = 0
        temp = []
        for j in range(len(citations)):
            # print("cita :",cita,"citations[j] :",citations[j])
            if citations[j] >= cita:
                count += 1
                # print("hit here")
            else:
                temp.append(citations[j])
                # print(temp)

        # print("cont :",count)
        if len(temp) > 0:
            max_temp = max(temp)
        else:
            max_temp = 0
        # print("max_temp :", max_temp)
        if max_temp <= cita and count > max_count and count <= cita:
            # print("count :",count,"cita :",cita,"max_count :",max_count)
            max_count = count

    return max_count