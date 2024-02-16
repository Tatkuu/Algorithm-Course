from collections import deque

def count(r):
    n, m = len(r), len(r[0])
    sx, sy, ex, ey = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if r[i][j] == 'A':
                sx, sy = i, j
            elif r[i][j] == 'B':
                ex, ey = i, j

    q = deque()
    q.append((sx, sy, 0))
    visited = set()
    visited.add((sx, sy))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while q:
        x, y, w = q.popleft()
        if x == ex and y == ey:
            return w
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if (nx, ny) in visited:
                continue
            if r[nx][ny] == '#':
                continue
            visited.add((nx, ny))
            if r[nx][ny] == '*':
                q.append((nx, ny, w + 1))
            else:
                q.appendleft((nx, ny, w))
                r[nx] = r[nx][:ny] + '*' + r[nx][ny+1:]

if __name__ == "__main__":
    r = ["########",
         "#*A*...#",
         "#.*****#",
         "#.**.**#",
         "#.*****#",
         "#..*.B.#",
         "########"]
    print(count(r)) # 2
