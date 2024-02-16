class Cities:
    def __init__(self, n):
        self.n = n
        self.roads = [[] for _ in range(n)]

    def add_road(self, a, b):
        self.roads[a-1].append(b-1)
        self.roads[b-1].append(a-1)

    def has_route(self, a, b):
        visited = [False] * self.n
        return self._has_route(a-1, b-1, visited)

    def _has_route(self, a, b, visited):
        if a == b:
            return True
        visited[a] = True
        for city in self.roads[a]:
            if not visited[city]:
                if self._has_route(city, b, visited):
                    return True
        return False

if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1,2)
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.has_route(1,5)) # False
    c.add_road(3,4)
    print(c.has_route(1,5)) # True
