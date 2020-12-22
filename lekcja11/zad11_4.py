# Porównaj czasy działania wybranych algorytmów dla listy zawierającej N różnych liczb, przy N = 10**2, 10**3, 10**4, 10**5, 10**6.
import random
import time

def swap(L, left, right):
    """Zamiana miejscami dwóch elementów."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item

def selectsort(L, left, right):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
        swap(L, i, k)

def insertsort(L, left, right):
    for i in range(left+1, right+1):   # L[left] jest posortowany
        item = L[i]
        j = i
        while j > left and L[j-1] > item:
            L[j] = L[j-1]   # robimy miejsce na item
            j = j-1
        L[j] = item

def shakersort(L, left, right):
    k = right
    while left < right:
        for j in range(right, left, -1):   # od prawej
            if L[j-1] > L[j]:
                swap(L, j-1, j)
                k = j
        left = k
        for j in range(left, right):   # od lewej
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                k = j
        right = k

def shellsort(L, left, right):
    h = (right - left) // 2
    while h > 0:
        for i in range(left + h, right + 1):
            for j in range(i, left + h - 1, -h):
                if L[j - h] > L[j]:
                    swap(L, j - h, j)
        h = h // 2

def quicksort(L, left, right):
    if left >= right:
        return
    swap(L, left, (left + right) // 2)   # element podziału
    pivot = left                      # przesuń do L[left]
    for i in range(left + 1, right + 1):   # podział
        if L[i] < L[left]:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)     # odtwórz element podziału
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

def mergesort(L, left, right):
    """Sortowanie przez scalanie."""
    if left < right:
        middle = (left + right) // 2   # wyznaczanie środka 
        mergesort(L, left, middle)
        mergesort(L, middle + 1, right)
        merge(L, left, middle, right)   # scalanie

def merge(L, left, middle, right):
    """Łączenie posortowanych sekwencji z wartownikami."""
    n1 = middle - left + 1
    n2 = right - middle
    A = [None] * (n1 + 1)   # o jeden więcej
    B = [None] * (n2 + 1)   # o jeden więcej
    for i in range(n1):
        A[i] = L[left + i]
    for i in range(n2):
        B[i] = L[middle + 1 + i]
    A[n1] = float("inf")   # wartownik
    B[n2] = float("inf")   # wartownik
    i, j = 0, 0
    for k in range(left, right+1):
        if A[i] <= B[j]:
            L[k] = A[i]
            i += 1
        else:
            L[k] = B[j]
            j += 1

sorting_algorithms = [selectsort, insertsort, shellsort, shakersort, quicksort, mergesort]

def measure_alg_time(alg):
	L = list(range(N**i))
	random.shuffle(L)
	start = time.time()
	alg(L, 0, len(L)-1)
	print('{0} w czasie {1:.5f}s'.format(alg.__name__, time.time()-start))

def compare_algorithms(i):
	print('\nDla N równego N**{0}:'.format(i))
	for sort_alg in sorting_algorithms:		
		measure_alg_time(sort_alg)

if __name__ == '__main__':
	N = 10
	for i in range(2, 7):
		compare_algorithms(i)