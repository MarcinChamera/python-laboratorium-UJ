import cmath

def solve2(a, b, c):
	"""Rozwiązywanie równania kwadratowego a * x * x + b * x + c = 0."""
	d = b ** 2 - 4 * a * c
	if d < 0:
		return 0
	if d == 0:
		return -b / (2 * a)
	return (-b - d) / (2 * a), (-b + d) / (2 * a)

if __name__ == '__main__':
	print(solve2(1, 2, 1))
	print(solve2(1, 5, 6))