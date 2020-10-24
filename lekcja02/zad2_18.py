from random import randint
big_number = randint(10**9, 10**10)
def zero_in_number(number):
	for digit in str(number):
		if digit is '0':
			return True
	return False

print(big_number)
print(zero_in_number(big_number))
