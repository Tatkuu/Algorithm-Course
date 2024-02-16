def count(s):
    count = 0
    char = ""
    add = 1
    for muuttuja in s:
        if (muuttuja not in char):
            char += muuttuja
            add = str.count(s, muuttuja, 0)
            count += (int)(add * (add + 1) / 2)
    return count

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abcd")) # 4
    print(count("ababca")) # 10
    