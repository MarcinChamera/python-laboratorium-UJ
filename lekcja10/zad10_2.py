# Poprawić implementację tablicową stosu tak, aby korzystała z wyjątków w przypadku pojawienia się błędu.
# Metoda pop() ma zgłaszać błąd w przypadku pustego stosu. Metoda push() ma zgłaszać błąd w przypadku przepełnienia stosu.
# Napisać kod testujący stos.
class Stack:

	def __init__(self, size=10):
		if size < 1:
			raise ValueError("Stack's size cannot be smaller than 1")
		self.items = size * [None]      # utworzenie tablicy
		self.n = 0                      # liczba elementów na stosie
		self.size = size

	def is_empty(self):
		return self.n == 0

	def is_full(self):
		return self.size == self.n

	def push(self, data):
		if self.is_full():
			 raise Exception("Stack is full, cannot add any more items")
		self.items[self.n] = data
		self.n += 1

	def pop(self):
		if self.is_empty():
			raise Exception("Cannot pop from an empty stack")
		self.n -= 1
		data = self.items[self.n]
		self.items[self.n] = None    # usuwam referencję
		return data

import unittest

class TestStack(unittest.TestCase):
	def setUp(self):
		self.stack = Stack(1)		

	def test_init(self):
		self.assertRaises(ValueError, lambda: Stack(0))

	def test_is_empty(self):      
		self.assertTrue(self.stack.is_empty())
		self.stack.push(1)
		self.assertFalse(self.stack.is_empty()) 

	def test_is_full(self):      
		self.assertFalse(self.stack.is_full())
		self.stack.push(1)
		self.assertTrue(self.stack.is_full())

	def test_push(self):
		self.stack.push(1)
		self.assertRaises(Exception, lambda: self.stack.push(2))

	def test_pop(self):
		self.assertRaises(Exception, lambda: self.stack.pop())

	def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy