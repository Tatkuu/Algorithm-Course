def count(s):
    count = 0
    char = ''
    add = 1
    for muuttuja in s:
        if muuttuja == char:
            add += 1
        else:
            add = 1       
        char = muuttuja
        count += add
    return count

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5