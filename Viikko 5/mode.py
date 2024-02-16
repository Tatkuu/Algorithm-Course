
class Mode:
    def __init__(self):
        self.numbers = []

    def add(self, x):
        self.numbers.append(x)
        counts = {k:self.numbers.count(k) for k in set(self.numbers)}
        modes = sorted(dict(filter(lambda x: x[1] == max(counts.values()), counts.items())).keys())
        return modes[0]
if __name__ == "__main__":
    m = Mode()
    print(m.add(3))
    print(m.add(2))
    print(m.add(2))
    print(m.add(5))
    print(m.add(5))
    print(m.add(5))
    print(m.add(6))
    print(m.add(6))
    print(m.add(6))
    print(m.add(6))
    print(m.add(1))
    print(m.add(1))
    print(m.add(1))
    print(m.add(1))
    print(m.add(1))