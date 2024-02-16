from itertools import product
def create(n):
    s = ""
    sana = "ABC"
    result = []
    keywords = [''.join(i) for i in product(sana, repeat = n)]
    for i in keywords:
        if "AA" in i or "BB" in i or "CC" in i:
            continue
        else:
            result.append(i)
    return result
if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AB,AC,BA,BC,CA,CB]
    print(len(create(5))) # 48
