class Cycles:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, a, b):
        self.graph[a-1].append(b-1)

    def check(self):
        visited = [False] * self.n
        stack = [False] * self.n

        for i in range(self.n):
            if not visited[i]:
                if self.dfs(i, visited, stack):
                    return True
        return False

    def dfs(self, node, visited, stack):
        visited[node] = True
        stack[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self.dfs(neighbor, visited, stack):
                    return True
            elif stack[neighbor]:
                return True

        stack[node] = False
        return False

if __name__ == "__main__":
    c = Cycles(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(1,3)
    c.add_edge(3,4)
    print(c.check()) # False
    c.add_edge(4,2)
    print(c.check()) # True
