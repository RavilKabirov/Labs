def all(N):
    for i in range(N, -1, -1):
        yield i
N = int(input())
x = all(N)
for j in x:
    print(j)