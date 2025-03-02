a = [1, 2, 3, 4, 5]
s = a[0]
for i in a:
    temp = 0
    for j in range(i):
        temp = sum([temp, s])
    s = temp
print(s)