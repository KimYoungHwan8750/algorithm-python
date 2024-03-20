from collections import deque


def bfs(graph, start_node):
    visited = set()  # 방문한 노드를 기록하기 위한 집합
    queue = deque([start_node])  # 시작 노드를 큐에 삽입

    while queue:  # 큐가 빌 때까지 반복
        current_node = queue.popleft()  # 큐에서 노드를 하나 꺼냄
        if current_node not in visited:  # 현재 노드를 방문하지 않았다면
            visited.add(current_node)  # 현재 노드를 방문했다고 표시
            print(current_node, end=" ")  # 현재 노드를 출력(탐색 순서 확인용)

            # 현재 노드에 연결된 모든 인접 노드를 큐에 삽입
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# 간단한 그래프 예시
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 'A' 노드부터 BFS 실행
bfs(graph, 'A')