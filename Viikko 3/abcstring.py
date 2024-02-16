def countmoves(arr1, arr2, i, j):
    if arr1 == arr2:
        return 0
    if i >= len(arr1) or j >= len(arr2):
        return 0
    if arr1[i] < arr2[j]:
        return 1 \
        + countmoves(arr1, arr2, i + 1, j + 1)
    return max(countmoves(arr1, arr2, i, j + 1),
               countmoves(arr1, arr2, i + 1, j))

def solve(lst):
    # dict that maps each list element to its index in the sorted list
    sorted_index = {elem: i for i, elem in enumerate(sorted(lst))}
    moves = 0
    for idx, elem in enumerate(lst):
        if idx != sorted_index[elem] + moves:
            moves += 1
    return moves
if __name__ == "__main__":
    print(solve("CCAABB")) # 4
    print(solve("CBACBA")) # 3
    print(solve("AAAA")) # 0