from random import random

def calc_pi(n=100):
	"""Obliczanie liczby pi metodą Monte Carlo.
	n oznacza liczbę losowanych punktów."""
	inside = 0
	for _ in range(n):
		x = random()
		y = random()
		if x ** 2 + y ** 2 <= 1:
			inside += 1
	pi = 4 * inside / n
	print('{0} iteracji : {1}'.format(n, pi))


if __name__ == '__main__':
	calc_pi(10)
	calc_pi(50)
	calc_pi()
	calc_pi(200)
	calc_pi(500)
	calc_pi(1000)
	calc_pi(2000)
	calc_pi(5000)
	calc_pi(10000)
	calc_pi(100000)
	calc_pi(1000000)