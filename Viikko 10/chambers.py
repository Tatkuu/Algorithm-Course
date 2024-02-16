def count(r):
    grid = [list(row) for row in r]
    n, m = len(grid), len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    room_count = 0


    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and grid[x][y] == '.'


    def bfs(x, y):
        queue = [(x, y)]
        visited[x][y] = True
        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == '.':
                room_count += 1
                bfs(i, j)

    return room_count

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3
