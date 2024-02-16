def count(coins):
    n = len(coins)
    max_sum = sum(coins)
    possible_sums = [False] * (max_sum + 1)
    possible_sums[0] = True

    for i in range(n):
        for j in range(max_sum, coins[i] - 1, -1):
            possible_sums[j] |= possible_sums[j - coins[i]]

    count = 0
    for i in range(1, max_sum + 1):
        if possible_sums[i]:
            count += 1

    return count


if __name__ == "__main__":
    print(count([3,4,5])) # 7
    print(count([1,1,2])) # 4
    print(count([2,2,2,3,3,3])) # 13
    print(count([42,5,5,100,1,3,3,7])) # 91
