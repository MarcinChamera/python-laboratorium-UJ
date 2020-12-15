# Poprawić metodę get(), aby w przypadku pustej kolejki zwracała wyjątek.
# Poprawić metodę put() w tablicowej implementacji kolejki,
# aby w przypadku przepełnienia kolejki zwracała wyjątek. Napisać kod testujący kolejkę.
class Queue:

    def __init__(self, size=5):
        if size < 1:
            raise ValueError("Queue's size cannot be smaller than 1")
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise Exception("The queue is full")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data

import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(1)       

    def test_init(self):
        self.assertRaises(ValueError, lambda: Queue(0))

    def test_is_empty(self):      
        self.assertTrue(self.queue.is_empty())
        self.queue.put(1)
        self.assertFalse(self.queue.is_empty()) 

    def test_is_full(self):      
        self.assertFalse(self.queue.is_full())
        self.queue.put(1)
        self.assertTrue(self.queue.is_full())

    def test_put(self):
        # self.queue.put(0)
        self.queue.put(1)
        self.assertRaises(Exception, lambda: self.queue.put(2))

    def test_get(self):
        self.assertRaises(Exception, lambda: self.queue.get())

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy