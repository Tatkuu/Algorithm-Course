def count(grid):
    n = len(grid)
    if grid[0][0] == "#" or grid[n-1][n-1] == "#":
        return -1
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = int(grid[0][0] == "@")
    for i in range(n):
        for j in range(n):
            if i > 0 and grid[i-1][j] != "#":
                dp[i][j] = min(dp[i][j], dp[i-1][j] + int(grid[i][j] == "@"))
            if j > 0 and grid[i][j-1] != "#":
                dp[i][j] = min(dp[i][j], dp[i][j-1] + int(grid[i][j] == "@"))
    return dp[n-1][n-1] if dp[n-1][n-1] != float('inf') else -1




if __name__ == "__main__":
    r = ["....@",
         "@##.#",
         ".##@#",
         ".@..#",
         "###@."]
    print(count(r)) # 2
