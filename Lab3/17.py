def is_pal(s):
    m = ""
    for i in range(len(s) - 1, 0 - 1, -1):
        m += s[i]
    if m == s:
        print("Yea")
    else:
        print("no")
    return
s = input()
is_pal(s)