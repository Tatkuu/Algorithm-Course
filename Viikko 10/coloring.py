class Coloring:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self,a,b):
        self.graph[a-1].append(b-1)
        self.graph[b-1].append(a-1)

    def check(self):
        def dfs(node, color):
            nonlocal colors
            colors[node] = color
            for neighbor in self.graph[node]:
                if colors[neighbor] == color:
                    return False
                if colors[neighbor] == 0 and not dfs(neighbor, -color):
                    return False
            return True

        colors = [0] * self.n
        for node in range(self.n):
            if colors[node] == 0 and not dfs(node, 1):
                return False
        return True

if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(3,4)
    c.add_edge(1,4)
    print(c.check()) # True
    c.add_edge(2,4)
    print(c.check()) # False
