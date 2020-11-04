# Summer/Winter - 지형 이동 예제만 통과..... 크루스카 알고리즘은 또뭐야

from collections import deque
import itertools

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

parent = {}
rank = {}
# 정점을 독립적인 집합으로 만든다.
def make_set(v):
    parent[v] = v
    rank[v] = 0
# 해당 정점의 최상위 정점을 찾는다.
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]
# 두 정점을 연결한다.
def union(v, u):
    root1 = find(v)
    root2 = find(u)
    if root1 != root2:
        # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1
def kruskal(graph):
    for v in graph['vertices']:
        make_set(v)
    mst = []
    edges = graph['edges']
    edges.sort()
    for edge in edges:
        weight, v, u = edge
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
    return mst


def bfs(graph, limit, x, y, visited):
    # print("bfs 들어옴")
    que = deque()
    que.append((x, y))
    visited[x][y] = True
    result = [[x,y,graph[x][y]]]
    while que:
        x, y = que.popleft()
        # print(que)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
            if abs(graph[nx][ny] - graph[x][y]) > limit:
                continue
            else:
                if not visited[nx][ny] :
                    visited[nx][ny] = True
                    que.append((nx, ny))
                    result.append([nx,ny,graph[nx][ny]])
    return result, visited

def solution(land, height):
    visited = [[False for col in range(len(land))] for row in range(len(land))]
    check = list(itertools.chain(*visited))
    result_list = []
    while False in check:
        for i in range(len(land)):
            for j in range(len(land)):
                if not visited[i][j] :
                    result, new_visited = bfs(land, height, i, j, visited)
                    result_list.append(result)
                    # print(result, new_visited)
                    check = list(itertools.chain(*new_visited))

    # print(result_list)
    gap_list = []
    gap_graph = {
        'vertices': [],
        'edges': []
    }
    for i in range(len(result_list)):
        gap_graph["vertices"].append(i)
        for j in range(len(result_list)):
            if i < j:
                min_gap = 10001
                for a in range(len(result_list[i])):
                    x = result_list[i][a][0]
                    y = result_list[i][a][1]
                    value = result_list[i][a][2]
                    for delta in range(4):
                        nx = x + dx[delta]
                        ny = y + dx[delta]
                        for b in range(len(result_list[j])):
                            if result_list[j][b][0] == nx and result_list[j][b][0] == ny:
                                target = abs(result_list[j][b][2] - value)
                                # print('target : ', target, 'value : ', value)
                                if min_gap > target:
                                    min_gap = target
                                    # print("min_gap :", min_gap)
                # print("--------------")
                gap_graph['edges'].append((min_gap,i,j))

    # print(gap_list)
    print(gap_graph)
    temp = kruskal(gap_graph)
    answer = 0
    for i in temp:
        answer += i[0]
    # print(temp)
    return answer

# print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))