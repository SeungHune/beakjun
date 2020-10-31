from collections import deque
import itertools

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, value, x, y, visited):
    # print("bfs 들어옴")
    que = deque()
    que.append([x, y])
    visited[x][y] = True
    result = [graph[x][y]]
    while que:
        # print(que)
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
            else:
                if not visited[nx][ny] and graph[nx][ny] == value :
                    visited[nx][ny] = True
                    que.append([nx, ny])
                    result.append(graph[nx][ny])
    # print(result)
    return result, visited

def solution(v):
    answer = [0] * 3
    visited = [[False for col in range(len(v))] for row in range(len(v))]
    check = list(itertools.chain(*visited))
    # print(visited)
    # print(check)
    result_list = []
    while False in check:
        for i in range(len(v)):
            for j in range(len(v)):
                if not visited[i][j]:
                    result, visited = bfs(v,v[i][j],i,j,visited)
                    # print(result, new_visited)
                    result_list.append(result)
                    check = list(itertools.chain(*visited))

    # print(result_list)
    for semi in result_list:
        if 0 in semi:
            answer[0] += 1
            continue
        elif 1 in semi:
            answer[1] += 1
            continue
        elif 2 in semi:
            answer[2] += 1
            continue
    return answer

print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))
print(solution([[0,0,1],[2,2,1],[0,0,0]]))