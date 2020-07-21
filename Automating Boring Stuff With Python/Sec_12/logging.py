# I could not understand the logging because it was not running due to circular error

def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


print(factorial(5))
