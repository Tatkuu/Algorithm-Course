class Components:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1

    def add_road(self, a, b):
        self.union(a - 1, b - 1)

    def count(self):
        return sum(1 for i in range(self.n) if self.parent[i] == i)

if __name__ == "__main__":
    c = Components(5)
    print(c.count())  # 5
    c.add_road(1, 2)
    c.add_road(1, 3)
    print(c.count())  # 3
    c.add_road(2, 3)
    print(c.count())  # 3
    c.add_road(4, 5)
    print(c.count())  # 2
