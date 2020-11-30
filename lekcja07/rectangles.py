from points import Point

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if x1 >= x2 or y1 >= y2:
            raise ValueError('x1 value needs to be lower than 2 and y1 needs to be lower than y2')
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return '[({0}, {1}), ({2}, {3})]'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return 'Rectangle({0}, {1}, {2}, {3})'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        return Point((self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.y)/2)

    def area(self):            # pole powierzchni
        return (self.pt2.y - self.pt1.y) * (self.pt2.x - self.pt1.x)

    def move(self, x, y):      # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other): # część wspólna prostokątów
        x2 = min(self.pt2.x, other.pt2.x) 
        x1 = max(self.pt1.x, other.pt1.x)
        y2 = min(self.pt2.y, other.pt2.y) 
        y1 = max(self.pt1.y, other.pt1.y)
        if x2 - x1 > 0 and y2 - y1 > 0:
            return Rectangle(x1, y1, x2, y2)
        return 0

    def cover(self, other):    # prostąkąt nakrywający oba
        x2 = max(self.pt2.x, other.pt2.x) 
        x1 = min(self.pt1.x, other.pt1.x)
        y2 = max(self.pt2.y, other.pt2.y) 
        y1 = min(self.pt1.y, other.pt1.y)
        return Rectangle(x1, y1, x2, y2) 

    def make4(self):           # zwraca krotkę czterech mniejszych
        ctr = self.center()
        return (
            Rectangle(self.pt1.x, ctr.y, ctr.x, self.pt2.y),
            Rectangle(ctr.x, ctr.y, self.pt2.x, self.pt2.y),
            Rectangle(self.pt1.x, self.pt1.y, ctr.x, ctr.y),
            Rectangle(ctr.x, self.pt1.y, self.pt2.x, ctr.y)
            )


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

    def test_intersection(self):
        self.assertEqual(self.rectangle.intersection(Rectangle(1, -2, 3, 1)), 0)
        self.assertEqual(self.rectangle.intersection(Rectangle(0, 1, 3, 3)), Rectangle(1, 2, 3, 3))

    def test_cover(self):
        self.assertEqual(self.rectangle.cover(Rectangle(1, -2, 3, 1)), Rectangle(1, -2, 3, 5))

    def test_make4(self):
        self.assertEqual(Rectangle(0, 0, 6, 4).make4(),
            (Rectangle(0, 2, 3, 4), Rectangle(3, 2, 6, 4), Rectangle(0, 0, 3, 2), Rectangle(3, 0, 6, 2)))

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy