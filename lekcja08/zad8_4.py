#Zaimplementować algorytm obliczający pole powierzchni trójkąta, jeżeli dane są trzy liczby będące długościami
#jego boków. Jeżeli podane liczby nie spełniają warunku trójkąta, to program ma generować wyjątek ValueError.
import math

def heron(a, b, c):
	"""Obliczanie pola powierzchni trójkąta za pomocą wzoru
	Herona. Długości boków trójkąta wynoszą a, b, c."""
	longest = max(a, b, c)
	other = {a, b, c} - {longest}
	if longest >= sum(other):
		raise ValueError("The longest side cannot be longer than the sum of two other sides")
	s = (a + b + c) / 2
	return math.sqrt(s * (s - a) * (s - b) * (s - c))

if __name__ == '__main__':
	print(heron(5, 6, 7))