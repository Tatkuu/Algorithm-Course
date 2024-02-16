class AllRoutes:
    def __init__(self, n):
        self.n = n
        self.graph = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            self.graph[i][i] = 0

    def add_road(self, a, b, x):
        if self.graph[a-1][b-1] > x:
            self.graph[a-1][b-1] = x
            self.graph[b-1][a-1] = x

    def get_table(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.graph[i][j] = min(self.graph[i][j], self.graph[i][k] + self.graph[k][j])
        for i in range(self.n):
            for j in range(self.n):
                if self.graph[i][j] == float('inf'):
                    self.graph[i][j] = -1
        return self.graph

if __name__ == "__main__":
    a = AllRoutes(4)
    a.add_road(1,2,2)
    a.add_road(1,3,5)
    a.add_road(2,3,1)
    print(a.get_table())
    # [[0,2,3,-1],[2,0,1,-1],[3,1,0,-1],[-1,-1,-1,0]]
