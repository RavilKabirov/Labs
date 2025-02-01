def rev(a):
    streng = ""
    los = ""
    for i in range(len(a) - 1, -1, -1):
        if a[i] != " ":
            los += a[i]
        else:
            for j in range(len(los) - 1, -1, -1):
                streng += los[j]
            streng += " "
            los = ""
    for j in range(len(los) - 1, -1, -1):
                streng += los[j]
    return streng
a = input()
print(rev(a))