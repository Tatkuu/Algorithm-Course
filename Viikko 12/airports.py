class Airports:
    def __init__(self, n):
        self.n = n
        self.graph = [[False] * n for _ in range(n)]

    def add_link(self, a, b):
        self.graph[a - 1][b - 1] = True

    def check(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.graph[i][k] and self.graph[k][j]:
                        self.graph[i][j] = True

        for i in range(self.n):
            visited = [False] * self.n
            self.dfs(i, visited)
            if not all(visited):
                return False
        return True

    def dfs(self, node, visited):
        visited[node] = True
        for neighbor, connected in enumerate(self.graph[node]):
            if connected and not visited[neighbor]:
                self.dfs(neighbor, visited)


if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1,2)
    a.add_link(2,3)
    a.add_link(1,3)
    a.add_link(4,5)
    print(a.check()) # False
    a.add_link(3,5)
    a.add_link(1,4)
    print(a.check()) # False
    a.add_link(5,1)
    print(a.check()) # True
