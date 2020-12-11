import cmath

def solve2(a, b, c):
	"""Rozwiązywanie równania kwadratowego a * x * x + b * x + c = 0."""
	if a == 0:
		return -c / b
	d = b ** 2 - 4 * a * c
	if d < 0:
		raise ValueError("ujemna delta")
		# return (None, None)
	if d == 0:
		return (-b / (2 * a), None)
	return ((-b - d) / (2 * a), (-b + d) / (2 * a))

if __name__ == '__main__':
	try:
		print(solve2(1, 1, 1))
	except ValueError as e:
		print(e)
	print(solve2(1, 2, 1))
	print(solve2(1, 5, 6))