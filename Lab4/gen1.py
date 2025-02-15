def square(N):
    for i in range(1, N + 1):
        yield i * i
N = int(input())
x = square(N)
for j in range(N):
    print(next(x))
