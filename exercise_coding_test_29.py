# 탐욕법 - 섬 연결하기

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

def solution(n, costs):
    answer = 0
    graph = {
        'vertices' : [],
        'edges' : []
    }
    for i in range(n):
        graph['vertices'].append(i)
    for cost in costs:
        graph['edges'].append((cost[2], cost[0], cost[1]))
    temp = kruskal(graph)
    for sub in temp:
        answer += sub[0]
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))