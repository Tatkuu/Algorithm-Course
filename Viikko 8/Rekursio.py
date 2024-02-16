import time

def f(n):
    if n <= 2:
        return n

    return f(n-1)+f(n-2)+f(n-3)

if __name__=="__main__":
    alku = time.time()
    print(f(30))
    loppu = time.time()
    print("aikaa kului", loppu-alku, "s")
