def unique(s):
    b = []
    for i in s:
        if i not in b:
            b.append(i)
    return b

s = [1, 4 ,2 ,1 ,2, 3 , 1 ,2 ,3 , 4, "dfd", "dfd", "fdgdf", True, False, True]
print(unique(s))