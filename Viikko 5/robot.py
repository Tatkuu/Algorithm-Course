def count(s):
    res = 1
    a = {}
    vertical = 0
    horizontal = 0
    a[vertical,horizontal] = 1
    for i in s:
        if i == 'L':
            vertical += 1
            if not (vertical,horizontal) in a:
                a[vertical,horizontal] = 1
                res += 1
        elif i == 'R':
            vertical -= 1
            if not (vertical,horizontal) in a:
                a[vertical,horizontal] = 1
                res += 1
        elif i == 'U':
            horizontal -= 1
            if not (vertical,horizontal) in a:
                a[vertical,horizontal] = 1
                res += 1
        elif i == 'D':
            horizontal += 1
            if not (vertical,horizontal) in a:
                a[vertical,horizontal] = 1
                res += 1
    return res

print(count("LULURDDL")) # 7
print(count("UUDLRR")) # 5
print(count("UDUDUDU")) # 2