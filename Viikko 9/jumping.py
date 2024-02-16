def apuf(porras, nporras, lista,a,b):

    if porras >= nporras:
        return porras == nporras

    if lista[porras] != -1:
        return lista[porras]

    aporras = apuf(porras + a, nporras, lista,a,b)
    bporras = apuf(porras + b, nporras, lista,a,b)
    lista[porras] = (aporras + bporras)

    return lista[porras]

def count(nportaat,a, b):


    lista = [-1 for _ in range(nportaat)]
    result = apuf(0, nportaat, lista,a,b)

    return int(result)

if __name__ == "__main__":
    print(count(47,1,2))
    print(count(4,1,2)) # 5
    print(count(10,2,5)) # 2
    print(count(10,6,7)) # 0
    print(count(30,3,5)) # 58
    print(count(50,2,3)) # 525456
