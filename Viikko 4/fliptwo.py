def solve(n,k):
    r = 1
    for i in range(0, k):
        if r == n - 1:
              r = 2
        elif r == n:
            r = 1
        else:
            r += 2
    return r
if __name__ == "__main__":
    print(solve(4,3)) # 4
    print(solve(12,5)) # 11
    print(solve(99,555)) # 11
