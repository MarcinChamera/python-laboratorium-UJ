import math

def solve2(a, b, c):
	"""Rozwiązywanie równania kwadratowego a * x * x + b * x + c = 0."""
	if a == 0:
		if b == 0:
			return (None, None)
		return (-c / b, None)
	d = b ** 2 - 4 * a * c
	if d < 0:
		raise ValueError("ujemna delta")
		# return (None, None)
	if d == 0:
		return (-b / (2 * a), -b / (2 * a))
	return ((-b - math.sqrt(d)) / (2 * a), (-b + math.sqrt(d)) / (2 * a))

if __name__ == '__main__':
	print(solve2(0, 2, 5))
	print(solve2(0, 0, 0))
	try:
		print(solve2(1, 1, 1))
	except ValueError as e:
		print(e)
	print(solve2(1, 2, 1))
	print(solve2(1, 5, 6))