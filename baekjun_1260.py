from collections import deque
#
# n,m,v = map(int,input().split())
# matrix = [[0] * (n + 1) for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     matrix[a][b] = 1
#     matrix[b][a] = 1
#
# print(matrix)
#
# def dfs(v, matrix, visited):
#     visited += [v]
#     print(visited)
#     for search_node in range(len(matrix[v])):
#         if matrix[v][search_node] == 1 and search_node not in visited:
#             dfs(search_node, matrix, visited)
#     return visited
# # print(dfs(v,matrix,[]))
#
# visited = [False] * (n + 1)
# # print(visited)
# # print(matrix[0])
# def bfs(matrix, start, visited):
#     que = deque([start])
#     visited[start] = True
#     result = []
#     while que :
#         v = que.popleft()
#         # print(v)
#         result.append(v)
#         print(matrix[v])
#         for i in range(n+1):
#             if matrix[v][i] == 1 and not visited[i]:
#                 que.append(i)
#                 visited[i] = True
#     return result
#
# print(bfs(matrix, v, visited))
# print(dfs(v,matrix,[]))

n,m,v = map(int, input().split())

matrix = [[0] * n for _ in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    print(a,b)
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

print(matrix)
visited = [False] * n
def bfs(graph, start, visited):
    que = deque([start-1])
    # print(que)
    visited[start-1] = True
    result = []
    while que:
        v = que.popleft()
        # print(v)
        result.append(v+1)
        # print(result)
        for i in range(n):
            print("v :", v)
            print("i :", i)
            print("graph[v][i] : ", graph[v][i], visited[i])
            if graph[v][i] == 1 and visited[i] == False:
                que.append(i)
                visited[i] = True
    return result

def dfs(graph, v, visited):
    visited += [v]
    for search_node in range(len(graph[v])):
        if graph[v][search_node] == 1 and search_node not in visited:
            dfs(graph, search_node, visited)
    return visited

print(bfs(matrix, v, visited))
print(dfs(matrix, v-1, []))