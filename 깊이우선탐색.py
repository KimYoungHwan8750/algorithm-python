"""
만약 노드가 방문하지 않았으면
노드를 출력하고
방문 목록에 노드를 추가
그래프에서 노드의 인접리스트를 순회하고
인접한 항목에 대해 깊이 우선 탐색 실시
"""
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
visited = set()

def dfs(graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour)

dfs(graph, "A")