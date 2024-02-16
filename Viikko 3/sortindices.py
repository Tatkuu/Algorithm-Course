def get(t):
    sort_data = [(i,x) for x,i in enumerate(t)]
    sort_data = sorted(sort_data)
    result = [x[1] for x in sort_data]
    return result

if __name__ == "__main__":
    print(get([1,2,4,3])) # [0,1,3,2]
    print(get([4,2,1,3])) # [2,1,3,0]
    print(get([6,2,8,5,3])) # [1,4,3,0,2]