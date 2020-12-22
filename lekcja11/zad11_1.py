# Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania. Przydatne są m.in. następujące rodzaje danych:
# (a) różne liczby int od 0 do N-1 w kolejności losowej,
# (b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
# (c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,
# (d) N liczb float w kolejności losowej o rozkładzie gaussowskim,
# (e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N).
import random
import math
import numpy as np

def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item

def func_a(N):
	L = list(range(N))
	random.shuffle(L)
	return L

def custom_shellsort(L, left, right):
    h = (right - left) // 2
    while h > right / 10:
        for i in range(left + h, right + 1):
            for j in range(i, left + h - 1, -h):
                if L[j - h] > L[j]:
                    swap(L, j - h, j)
        h = h // 2

def func_b(N):
	L = func_a(N)
	custom_shellsort(L, 0, len(L)-1)
	return L

def func_c(N):
	L = func_b(N)
	L.reverse()
	return L

def func_d(N):
	mu, sigma = 0, 0.1 # mean and standard deviation
	return np.random.normal(mu, sigma, N)

def func_e(N):
	return [random.randint(0, math.sqrt(N)) for _ in range(N)] 

funcs = [func_a, func_b, func_c, func_d, func_e]

if __name__ == '__main__':
	N = 100
	for func in funcs:
		print('{0}:\n'.format(func.__name__), func(N), '\n')