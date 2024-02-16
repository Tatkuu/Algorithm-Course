def f(n):

    if n <= 2:
        return 1

    return 1+f(n-1)+f(n-2)+f(n-3)

if __name__=="__main__":
    print(f(30))
