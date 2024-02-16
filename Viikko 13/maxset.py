class MaxSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.max_size = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, a, b):
        a_root = self.find(a - 1)
        b_root = self.find(b - 1)

        if a_root != b_root:
            if self.rank[a_root] > self.rank[b_root]:
                self.parent[b_root] = a_root
                self.rank[a_root] += self.rank[b_root]
            else:
                self.parent[a_root] = b_root
                self.rank[b_root] += self.rank[a_root]

            self.max_size = max(self.max_size, self.rank[a_root], self.rank[b_root])

    def get_max(self):
        return self.max_size


if __name__ == "__main__":
    m = MaxSet(100000)
    m.merge(73846,95230)
    m.merge(65689,91281)
    print(m.get_max())
    m.merge(56793,63652)
    m.merge(54686,67495)
    m.merge(46393,62264)
    m.merge(80760,96970)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(91852,98254)
    m.merge(69907,74715)
    m.merge(91092,91882)
    print(m.get_max())
    m.merge(41193,70278)
    print(m.get_max())
    m.merge(4474,49377)
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    print(m.get_max())
    m.merge(58372,93525)
