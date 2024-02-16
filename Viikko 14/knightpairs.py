from collections import defaultdict

def count(r):
    def possible_moves(x, y):
        moves = [(x - 2, y - 1), (x - 2, y + 1),
                 (x - 1, y - 2), (x - 1, y + 2),
                 (x + 1, y - 2), (x + 1, y + 2),
                 (x + 2, y - 1), (x + 2, y + 1)]
        return [(i, j) for i, j in moves if 0 <= i < 8 and 0 <= j < 8]

    def bipartite_match(graph, u, match, visited):
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                if match[v] == (-1, -1) or bipartite_match(graph, match[v], match, visited):
                    match[v] = u
                    return True
        return False

    def max_bipartite_matching(graph):
        match = defaultdict(lambda: (-1, -1))
        result = 0
        for u in graph:
            visited = defaultdict(bool)
            if bipartite_match(graph, u, match, visited):
                result += 1
        return result

    graph = defaultdict(list)
    for i in range(8):
        for j in range(8):
            if r[i][j] == '*':
                for x, y in possible_moves(i, j):
                    if r[x][y] == '*':
                        if (i + j) % 2 == 0:
                            graph[(i, j)].append((x, y))

    return max_bipartite_matching(graph)

if __name__ == "__main__":
    r = [".***..*.",
         "**.*..**",
         ".*..****",
         "...***..",
         "**..*.**",
         "*..**.**",
         ".*..*...",
         "..*...**"]
    print(count(r))  # 15
