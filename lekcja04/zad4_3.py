def factorial(n):
    if n < 0:
        print('Incorrect number')
    if n == 0:
    	return 1
    x = 1
    for i in range(2, n+1):
        x *= i 
    return x

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))