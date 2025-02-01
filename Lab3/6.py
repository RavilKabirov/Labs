def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 15, 3, 7, 19, 20, 23, 29, 35, 40]

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers:", prime_numbers)
