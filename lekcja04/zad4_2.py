# ZADANIE 4.2
# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji,
# które zwracają pełny string przez return.

# ZADANIE 3.5
# Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć
# liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod
# znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

# |....|....|....|....|....|....|....|....|....|....|....|....|
# 0    1    2    3    4    5    6    7    8    9   10   11   12

def draw_measure(length):
	measure_str = '|....' * (length - 1) + '|'
	numbers = list(map(str,range(length+1)))
	numbers_str = number ' ' * (5 - len(number)) 

draw_measure(12)
