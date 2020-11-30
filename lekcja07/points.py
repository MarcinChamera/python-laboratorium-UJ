from math import sqrt

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return '({0}, {1})'.format(self.x, self.y)

    def __repr__(self):        # zwraca string "Point(x, y)"
        return 'Point({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other):   # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):   # obsługa point1 != point2
        return not (self.x == other.x and self.y == other.y)

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return self.x * other.x + self.y * other.y

    def cross(self, other):    # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return sqrt(self.x ** 2 + self.y ** 2)

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): 

    def setUp(self):
        self.point = Point(2,1)

    def test_print(self):      # test str() i repr()
        self.assertEqual(Point.__str__(self.point), '(2, 1)')
        self.assertEqual(Point.__repr__(self.point), 'Point(2, 1)') 

    def test_cmp(self):
        self.assertTrue(Point(2,1) == Point(2,1))
        self.assertFalse(Point(2,1) == Point(1,2))
        self.assertTrue(Point(2,1) != Point(1,2))
        self.assertFalse(Point(2,1) != Point(2,1))

    def test_add(self):   # musi działać porównywanie
        self.assertEqual(Point(2,1) + Point(1,3), Point(3,4))

    def test_sub(self):
        self.assertEqual(Point(2,1) - Point(1,3), Point(1,-2))

    def test_mul(self):
        self.assertEqual(Point(2,1) * Point(1,3), 5)

    def test_cross(self):
        self.assertEqual(self.point.cross(Point(1,3)), 5)

    def test_length(self):
        self.assertEqual(self.point.length(), sqrt(5))

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy