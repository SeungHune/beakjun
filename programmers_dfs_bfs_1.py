from collections import deque
import copy

def bfs(graph, start, visited):
    # print("들어왔다. 시작은 :",start)
    que = deque([start])
    visited[start] = 0
    result = []
    while que:
        v = que.popleft()
        result.append(v)
        # print(result)
        # print(graph[v])
        for i in range(len(graph[v])):
            if visited[i] == 1 and graph[v][i] == 1:
                que.append(i)
                visited[i] = 0
    return result

def solution(n, computers):
    answer = 0
    visited = [1] * n
    for i in range(n):
        if sum(visited) == 0:
            break
        print("bfs 진행---------------")
        before = copy.deepcopy(visited)
        bfs(computers, i, visited)
        after = copy.deepcopy(visited)
        print("before :",before)
        print("after :", after)
        if before != after:
            answer += 1
    # print(visited)
    return answer

print(solution(3, [[1, 1, 0],
                   [1, 1, 0],
                   [0, 0, 1]]))
print(solution(3, [[1, 1, 0],
                   [1, 1, 1],
                   [0, 1, 1]]))
print(solution(3, [[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]]))
# print(solution())