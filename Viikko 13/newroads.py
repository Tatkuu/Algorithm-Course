class NewRoads:
    def __init__(self,n):
        self.n = n
        self.roads = []

    def add_road(self,a,b,x):
        self.roads.append((a,b,x))

    def min_cost(self):
        self.roads.sort(key=lambda x: x[2])

        sets = [{i} for i in range(1, self.n+1)]

        total_cost = 0

        for road in self.roads:
            a, b, x = road

            set_a = None
            set_b = None
            for s in sets:
                if a in s:
                    set_a = s
                if b in s:
                    set_b = s

            if set_a is set_b:
                continue

            sets.remove(set_a)
            sets.remove(set_b)
            sets.append(set_a.union(set_b))
            total_cost += x

            if len(sets) == 1:
                return total_cost

        return -1

if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1,2,2)
    n.add_road(1,3,5)
    print(n.min_cost()) # -1
    n.add_road(3,4,4)
    print(n.min_cost()) # 11
    n.add_road(2,3,1)
    print(n.min_cost()) # 7
