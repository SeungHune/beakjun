from collections import deque

def bfs(start, graph, visited):
    que = deque([start])
    visited[start] = True
    result = []
    while que:
        v = que.popleft()
        for i in range(len(graph)):
            if graph[v][i] == 1 and visited[i] == False:
                que.append(i)
                visited[i] = True
    return result

def solution(n, edge):
    answer = 0
    graph = [[0] * n  for _ in range(n)]
    for line in edge:
        graph[line[0]-1][line[1]-1] = 1
        graph[line[1]-1][line[0]-1] = 1
    print(graph)
    visited = [False] * n
    print(visited)
    answer = bfs(0,graph,visited)

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))