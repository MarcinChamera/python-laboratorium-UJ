# Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności.
# Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.
import random

class RandomQueue():

	def __init__(self, size=10):
		self.items = size * [None]
		self.n = 0   # pierwszy wolny indeks
		self.size = size

	def is_empty(self):
		return self.n == 0

	def is_full(self):
		return self.size == self.n

	def insert(self, data):
		if self.n == self.size:
			raise Exception("Queue's full")
		self.items[self.n] = data
		self.n += 1

	def remove(self):
		if self.n == 0:
			raise Exception("Queue's empty")
		random_i = random.randint(0, self.n - 1)
		self.n -= 1
		data = self.items[random_i]
		self.items[random_i] = self.items[self.n]
		self.items[self.n] = None   # usuwamy referencję
		return data

	def clear(self):     # czyszczenie listy
		self.items = self.size * [None]
		self.n = 0

if __name__ == '__main__':
	random_queue = RandomQueue()
	for i in range(5):
		random_queue.insert(i)
	for _ in range(5):
		print(random_queue.remove())