import math
def is_prime(func):
    def wrapper(*args):
        result = func(*args)

        if is_prime_number(result):
            print("Простое")
        else:
            print("Составное")

        return result

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

def is_prime_number(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


result = sum_three(2, 3, 6)
print(result)
