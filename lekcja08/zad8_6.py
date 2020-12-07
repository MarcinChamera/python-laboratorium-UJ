# Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j). 
# Porównać z wersją rekurencyjną programu. Wskazówka: Wykorzystać tablicę dwuwymiarową (np. słownik)
# do przechowywania wartości funkcji. Wartości w tablicy wypełniać kolejno wierszami.

# P(0, 0) = 0.5,
# P(i, 0) = 0.0 dla i > 0,
# P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.
import time

def P_recursive(i, j):
	if i == 0 and j == 0:
		return 0.5
	if i > 0 and j == 0:
		return 0
	if i == 0 and j > 0:
		return 1
	return 0.5 * (P_recursive(i-1, j) + P_recursive(i, j-1))

def P_dynamic(i, j):
	P = [[0 for x in range(i+1)] for y in range(j+1)]
	for x in range(len(P[0])): 
		P[0][x] = 1
	P[0][0] = 0.5
	for x in range(1, i+1):
		for y in range(1, j+1):
			P[x][y] = 0.5 * (P[x-1][y] + P[x][y-1])
	return P[i][j]

if __name__ == '__main__':
	i = 12
	j = 12
	start_recursive = time.time()
	recursive_result = P_recursive(i, j)
	print('Wynik rekurencyjnie dla i={0} j={1} równy {2}, czas={3:.2f}s'.format(i, j, recursive_result, time.time() - start_recursive))
	start_dynamic = time.time()
	dynamic_result = P_dynamic(i, j)
	print('Wynik dynamicznie dla i={0} j={1} równy {2}, czas={3:.2f}s'.format(i, j, dynamic_result, time.time() - start_dynamic))