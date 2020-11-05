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
	measure_str = '|....' * length + '|'
	numbers = list(map(str,range(length+1)))
	numbers_str = numbers[0]
	for number in numbers[1:]:
		numbers_str += ' ' * (5 - len(number)) + number
	return measure_str + '\n' + numbers_str

print(draw_measure(12))

# ZADANIE 3.6
# Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:

# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   | 
# +---+---+---+---+

def draw_rectangle(width, height):
	rectangle_horizontal = '+' + width * '---+' + '\n'
	rectangle_one_height = '|' + width * '   |' + '\n'
	return rectangle_horizontal + height * (rectangle_one_height + rectangle_horizontal)

print(draw_rectangle(4, 2))