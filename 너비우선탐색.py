from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
"""
큐에 시작 노드를 넣는다.
큐가 있는 동안
노드가 방문한 적 없다면
노드를 출력하고 방문 목록에 노드를 담는다.
그래프[노드]를 순회하며 인접 리스트들을 확인한다
인접 리스트가 방문 목록에 없으면
큐에 인접 목록을 추가한다
"""

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

bfs(graph, "A")
# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#
#     while queue:
#         node = queue.popleft()  # 큐의 왼쪽 끝에서 요소를 제거하고 반환
#         if node not in visited:
#             print(node, end=' ')
#             visited.add(node)
#             for neighbour in graph[node]:
#                 if neighbour not in visited:
#                     queue.append(neighbour)
#
#
# # 사용 예
# bfs(graph, 'A')