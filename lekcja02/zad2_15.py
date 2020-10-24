from random import sample
L = sample(range(1, 10), 5)
number_string = ''
for number in L:
	number_string += str(number)
print(number_string)
