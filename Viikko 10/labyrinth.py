from collections import deque

def count(r):
    n = len(r)
    m = len(r[0])
    start = end = None
    visited = set()

    for i in range(n):
        for j in range(m):
            if r[i][j] == "A":
                start = (i, j)
            elif r[i][j] == "B":
                end = (i, j)

    if start is None or end is None:
        return -1

    q = deque([(start, 0)])
    visited.add(start)

    while q:
        current, steps = q.popleft()

        if current == end:
            return steps

        i, j = current
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for neighbor in neighbors:
            if neighbor[0] < 0 or neighbor[0] >= n or neighbor[1] < 0 or neighbor[1] >= m:
                continue
            if r[neighbor[0]][neighbor[1]] == "#" or neighbor in visited:
                continue
            q.append((neighbor, steps+1))
            visited.add(neighbor)

    return -1


if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7
