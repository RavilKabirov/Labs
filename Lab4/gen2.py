def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i 

n = int(input())
x = even_numbers(n)

first = True  
for num in x:
    if not first:
        print(", ", end="")  
    print(num, end="")  
    first = False  
 
