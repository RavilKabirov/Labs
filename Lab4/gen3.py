def div34(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i 

n = int(input())
x = div34(n)

for num in x:
    
    print(num)  
 