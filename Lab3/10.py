def is_prime(numbers):
    flag = True
    for number in numbers:
        if number < 2:
            flag = False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                flag = False
                break
        if flag == True:
            print(number)
        flag = True
    

numbers = [10, 15, 3, 7, 19, 20, 23, 29, 35, 40]
is_prime(numbers)
