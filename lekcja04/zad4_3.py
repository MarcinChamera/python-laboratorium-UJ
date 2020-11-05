def factorial(n):
    if n < 0:
        print('Incorrect number')
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * factorial(n-1)


print(factorial(4))