def count(t):
    count = 1

    t.sort()
    #[1,3,4,5]
    for i in range(0, len(t) - 1):
        if t[i + 1] > t[i] + 1 or t[i] + 1 <= t[i + 1] and i == len(t) - 1:
            count += 1
    return count

if __name__ == "__main__":
    print(count([4,1,5,3,3])) # 2
    print(count([4,2,1,3])) # 1
    print(count([5,2,7,6,3,9])) # 3