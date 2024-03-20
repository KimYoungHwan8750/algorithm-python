graph = {
    1: [5, 2],
    2: [3],
    3: [4],
    4: [2],
    5: [6],
    6: [],
}

explored = set()


def dfs(explored, node, graph):
    print(node)
    explored.add(node)
    for n in graph[node]:
        if n not in explored:
            dfs(explored, n, graph)

dfs(explored, 1, graph)