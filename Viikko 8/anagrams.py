import itertools
from itertools import permutations
def create(n):
    results = []
    words = list(itertools.permutations(n))
    words = [''.join(permutation) for permutation in words]
    for i in words:
        if i not in results:
            results.append(i)
        else:
            continue
    return sorted(results)
if __name__ == "__main__":
    print(create("ab")) # [ab,ba]
    print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    print(len(create("aybabtu"))) # 1260
