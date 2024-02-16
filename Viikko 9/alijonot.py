import random
def f(taulu,n):
    pisin = [0]
    for k in range(n):
        pisin.append(0)
        pisin[k] = 1
        for x in range(k):
            if taulu[x] < taulu[k] and pisin[x]+1 > pisin[k]:
                pisin[k] = pisin[x]+1
    pisin = sorted(pisin)
    return pisin[-1]
if __name__=="__main__":
    taulu = []
    for i in range(5000):
        taulu.append(random.randint(0,5000))
    print(f(taulu,5000))
