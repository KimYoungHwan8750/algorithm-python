"""
만약 노드가 방문하지 않았으면
노드를 출력하고
방문 목록에 노드를 추가
그래프에서 노드의 인접리스트를 순회하고
인접한 항목에 대해 깊이 우선 탐색 실시
"""
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
visited_dfs = set()
visited_bfs = set()

def dfs(graph, node):
    if node not in visited_dfs:
        print(node)
        visited_dfs.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour)

dfs(graph, "A")

print("-------------")

def bfs(graph, start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited_bfs:
            print(node)
            visited_bfs.add(node)
            for neighbour in graph[node]:
                queue.append(neighbour)

bfs(graph, "A")