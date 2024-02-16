def count(t):
    arr = [0] * len(t)
    arr[0] = t[0]
    arr2 = [0] * len(t)
    arr2[len(t) - 1] = t[len(t) - 1]
    count = 0

    for i in range(1, len(t)):
        if t[i] > arr[i - 1]:
            arr[i] = t[i]
        else:
            arr[i] = arr[i - 1]
    for i in range(len(t)-2, -1, -1):
        if t[i] < arr2[i + 1]:
            arr2[i] = t[i]
        else:
            arr2[i] = arr2[i + 1]
    for i in range(1, len(t)):
        if arr[i - 1] < arr2[i]:
            count += 1
    return count

if __name__ == "__main__":
    print(count([1, 499999999, 500000000, 500000000, 1000000000])) # 0  
    print(count([5,4,3,2,1])) # 0
    print(count([2,1,2,5,7,6,9])) # 3
    print(count([3, 1, 4, 3, 5])) # 1
    print(count([2, 2, 4, 9, 6])) # 1
    print(count([-7, 1, 5, 2, -4, 3, 0])) # 1
