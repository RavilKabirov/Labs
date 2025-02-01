def histogram(s):
    for i in s:
        for j in range(0, i):
            if j != i - 1:
                print("*", end="")
            else:
                print("*", end="\n")
        


histogram([4, 9, 7])