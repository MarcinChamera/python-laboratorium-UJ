from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return '[({0}, {1}), ({2}, {3})]'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return 'Rectangle({0}, {1}, {2}, {3})'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):   # obsługa rect1 != rect2
        return not (self.pt1 == other.pt1 and self.pt2 == other.pt2)

    def center(self):          # zwraca środek prostokąta
        return Point((self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.y)/2)

    def area(self):            # pole powierzchni
        return (self.pt2.y - self.pt1.y) * (self.pt2.x - self.pt1.x)

    def move(self, x, y):      # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase): 
    def setUp(self):
        self.rectangle = Rectangle(1, 2, 3, 5)

    def test_print(self):      # test str() i repr()
        self.assertEqual(Rectangle.__str__(self.rectangle), '[(1, 2), (3, 5)]')
        self.assertEqual(Rectangle.__repr__(self.rectangle), 'Rectangle(1, 2, 3, 5)') 

    def test_cmp(self):
        self.assertTrue(self.rectangle == Rectangle(1, 2, 3, 5))
        self.assertFalse(self.rectangle == Rectangle(1, 2, 3, 4))
        self.assertTrue(self.rectangle != Rectangle(1, 3, 4, 6))
        self.assertFalse(self.rectangle != Rectangle(1, 2, 3, 5))

    def test_center(self):
        self.assertEqual(Point(2, 3.5), self.rectangle.center())

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 6)

    def test_move(self):

        self.assertEqual(self.rectangle.move(2, 3), Rectangle(3, 5, 5, 8))

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy