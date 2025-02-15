def squares(T, N):
    for i in range(T, N + 1):
        yield i * i
T = int(input())
N = int(input())

x = squares(T, N)
for j in x:
    print(j)