class Download:
    def __init__(self, n):
        self.n = n
        self.matriisi = [[0] * (self.n + 1) for _ in range(self.n + 1)]
        self.seen = [False] * (self.n + 1)
        self.polku = []
        self.found = False
        self.summa = []

    def add_link(self, a, b, x):
        self.matriisi[a][b] += x

    def dfs(self, a, b, current_flow=float('inf')):
        if a == b:
            self.found = True
            return current_flow

        self.seen[a] = True
        for i in range(1, self.n + 1):
            if not self.seen[i] and self.matriisi2[a][i] > 0:
                min_flow = min(current_flow, self.matriisi2[a][i])
                flow = self.dfs(i, b, min_flow)
                if flow > 0:
                    self.matriisi2[a][i] -= flow
                    self.matriisi2[i][a] += flow
                    return flow

        return 0

    def calculate(self, a, b):
        self.polku = []
        self.summa = []
        self.matriisi2 = [x[:] for x in self.matriisi]

        self.a = a
        flow = float('inf')
        total_flow = 0

        while flow > 0:
            self.seen = [False] * (self.n + 1)
            flow = self.dfs(a, b)
            total_flow += flow

        return total_flow


if __name__ == "__main__":
    d = Download(5)
    d.add_link(2,5,5)
    d.add_link(3,5,3)
    d.add_link(3,2,3)
    d.add_link(2,1,6)
    print(d.calculate(4,3))
    d.add_link(5,4,4)
    d.add_link(4,3,4)
    print(d.calculate(3,5))
    print(d.calculate(1,4))
    print(d.calculate(1,4))
