# Napisać program, który na listę L wstawi n liczb wylosowanych z zakresu od 0 do k-1.
# Następnie program wylosuje liczbę y z tego samego zakresu i znajdzie wszystkie jej
# wystąpienia na liście L przy pomocy wyszukiwania liniowego. [n=100, k=10]
import random

def linear_search(L, left, right, y):
    """Wyszukiwanie liniowe w ciągu."""
    i = left
    while i <= right:
        if y == L[i]:
            return i
        i += 1
    return None

def func(L, k, n):
	for _ in range(n):
		L.append(random.randint(0, k-1))
	y = random.randint(0, k-1)
	start = 0
	counter = 0
	while start < len(L) - 1:
		result = linear_search(L, start + 1, len(L) - 1, y)
		if result is None:
			break
		counter += 1
		start = result
	return y, counter

if __name__ == '__main__':
	L = []
	n = 100
	k = 10
	L2 = [random.randint(0, k-1) for _ in range(n//2)]
	y, counts = func(L, k, n)
	print('Liczba {0} znaleziona w liscie\n{1}\n{2} razy'.format(y, L, counts))
	y2, counts2 = func(L2, k, n)
	print('\nLiczba {0} znaleziona w liscie\n{1}\n{2} razy'.format(y2, L2, counts2))
