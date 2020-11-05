def sum_seq(sequence):
	counter = 0
	for item in sequence:
		if isinstance(item, (list, tuple)):
			counter += sum_seq(item)
		else:
			counter += item
	return counter

print(sum_seq([1, 3, [4, 6], (2, (3, 3)), 9]))   
