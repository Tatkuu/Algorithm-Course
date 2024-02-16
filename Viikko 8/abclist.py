from itertools import product
def create(n):
    sana = "ABC"
    keywords = [''.join(i) for i in product(sana, repeat = n)]
    return keywords
if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AA,AB,AC,BA,BB,BC,CA,CB,CC]
    print(len(create(5))) # 243
