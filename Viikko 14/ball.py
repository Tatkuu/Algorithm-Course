class Ball:
    def __init__(self, n):
        self.graph = [[0] * (n + 1) for _ in range(n + 1)]
        self.m1 = n
        self.m2 = n

    def add_pair(self, k, v):
        self.graph[k][v] = 1


    def calculate(self):
        self.mSaa = [-1] * (self.m1 + 1)
        parit = 0
        for k in range(1, self.m2 + 1):
            paired = [False] * (self.m1 + 1)
            if self.dfs(k, paired):
                parit += 1

        return parit

    def dfs(self, k, paired):
        for v in range(1, self.m1 + 1):
            if self.graph[k][v] == 1 and not paired[v]:
                paired[v] = True
                if self.mSaa[v] == -1 or self.dfs(self.mSaa[v], paired):
                    self.mSaa[v] = k
                    return True
        return False

if __name__ == "__main__":
    b = Ball(4)
    print(b.calculate()) # 0
    b.add_pair(1,2)
    print(b.calculate()) # 1
    b.add_pair(1,3)
    b.add_pair(3,2)
    print(b.calculate()) # 2
