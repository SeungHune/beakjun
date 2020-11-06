# 깊이/너비 우선 탐색 - 여행경로
from collections import deque

def bfs(tickets, visited, start):
    que = deque([start])
    visited[tickets.index(start)] = True
    result = []
    while que:
        v = que.popleft()
        result.append(v)
        for ticket in tickets:
            if ticket[0] == v[1] and not visited[tickets.index(ticket)]:
                que.append(ticket)
                visited[tickets.index(ticket)] = True
                break
    return result

def solution(tickets):
    temp_ans = []
    visited = [False] * len(tickets)

    for ticket in tickets:
        if ticket[0] == "ICN":
            result = bfs(tickets, visited, ticket)
            # print(result)
            # print(visited)
            if len(result) == len(tickets):
                # print("여기오나?")
                temp = []

                for i in range(len(result)):
                    if i == len(result)-1:
                        temp.append(result[i][0])
                        temp.append(result[i][1])
                    else:
                        temp.append(result[i][0])
                temp_ans.append(temp)

            visited = [False] * len(tickets)
            continue

    # print(temp_ans)
    if len(temp_ans) == 1:
        answer = temp_ans[0]
    else:
        temp_ans.sort()
        answer = temp_ans[0]
    return answer

# print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))