class Frac:
    """Klasa reprezentująca ułamki."""
    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        if y == 0:
        	raise ValueError('Denumerator cannot be 0!')
        self.x = x
        self.y = y

    # Metoda, której używałoby się, przekazując jako argument other typu float, a która zwracałaby ułamek
    def frac_from_float(self, other):
        ratio = other.as_integer_ratio()
        return Frac(ratio[0], ratio[1])

    def gcd(self, a, b):
	    r= a % b
	    while r:
	        a = b
	        b = r
	        r = a % b
	    return b

    def polish(self, num, den):
        if num == 0:
            return Frac(0, den)
        gcd_res = self.gcd(num, den)
        num /= gcd_res
        den /= gcd_res
        return Frac(num, den)

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        return '{}'.format(self.x) if self.y == 1 else '{}/{}'.format(self.x, self.y)


    def __repr__(self):        # zwraca "Frac(x, y)"
        return 'Frac({0}, {1})'.format(self.x, self.y)

    # Python 2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        if isinstance(other, int):
            other = Frac(other)
        if self.y == other.y: 
            return self.x == other.x
        return self.x * other.y == other.x * self.y

    def __ne__(self, other):
        if self.y == other.y: 
            return self.x != other.x
        return self.x * other.y != other.x * self.y

    def __lt__(self, other):
        if self.y == other.y: 
            return self.x < other.x
        return self.x * other.y < other.x * self.y

    def __le__(self, other):
        if self.y == other.y: 
        	return self.x <= other.x
        return self.x * other.y <= other.x * self.y

    def __gt__(self, other):
        if self.y == other.y: 
        	return self.x > other.x
        return self.x * other.y > other.x * self.y

    def __ge__(self, other):
        if self.y == other.y: 
        	return self.x >= other.x
        return self.x * other.y >= other.x * self.y

    def __add__(self, other):  # frac1+frac2, frac+int
    	if isinstance(other, int):
    		numerator = self.x + other * self.y
    		denumerator = self.y
    	elif isinstance(other, Frac):
    		numerator = self.x * other.y + other.x * self.y
    		denumerator = self.y * other.y
    	return self.polish(numerator, denumerator)

    __radd__ = __add__              # int+frac

    def __sub__(self, other):  # frac1-frac2, frac-int
    	if isinstance(other, int):
    		numerator = self.x - other * self.y
    		denumerator = self.y 
    	elif isinstance(other, Frac):
    		numerator = self.x * other.y - other.x * self.y
    		denumerator = self.y * other.y
    	return self.polish(numerator, denumerator)

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        numerator = self.y * other - self.x
        denumerator = self.y
        return self.polish(numerator, denumerator)

    def __mul__(self, other):  # frac1*frac2, frac*int
        if isinstance(other, Frac):
            numerator = self.x * other.x
            denumerator = self.y * other.y 
        elif isinstance(other, int):
            numerator = self.x * other
            denumerator = self.y
        return self.polish(numerator, denumerator)

    __rmul__ = __mul__              # int*frac

    def __div__(self, other):  # frac1/frac2, frac/int, Python 2
        if isinstance(other, Frac):
            numerator = self.x * other.y 
            denumerator = self.y * other.x
        elif isinstance(other, int):
            if other == 0:
                raise ValueError('Cannot divide by 0!')
            numerator =  self.x
            denumerator = self.y * other
        return self.polish(numerator, denumerator)


    def __rdiv__(self, other): # int/frac, Python 2
    	numerator = other * self.y
    	denumerator = self.x
    	return self.polish(numerator, denumerator)

    def __truediv__(self, other):  # frac1/frac2, frac/int, Python 3
        if isinstance(other, Frac):
            numerator = self.x * other.y
            denumerator = self.y * other.x
        elif isinstance(other, int):
            if other == 0:
                raise ValueError('Cannot divide by 0!')
            numerator =  self.x
            denumerator = self.y * other
        return self.polish(numerator, denumerator)

    def __rtruediv__(self, other):  # int/frac, Python 3
        numerator = other * self.y
        if self.x == 0:
            raise ValueError('Cannot divide by 0!')
        denumerator = self.x
        return self.polish(numerator, denumerator)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):         # -frac = (-1)*frac
    	return (-1)*self

    def __invert__(self):      # odwrotnosc: ~frac
        if self.x == 0:
            raise ValueError('Denumerator cannot be 0!')
        self.x, self.y = self.y, self.x
        return self

    def __float__(self):       # float(frac)
    	return self.x / self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        assert set([2]) == set([2.0])

# Kod testujący moduł.

f1 = Frac(1, 2)
f2 = Frac(1, 3)
f3 = Frac(2, 7)
f4 = Frac(5, 24)
f5 = Frac(0, 24)
f6 = Frac(3)
f7 = Frac(-1, 2)
f8 = Frac(1, -2)
i1 = 3
i2 = -3
i3 = 0

import unittest

class TestFractions(unittest.TestCase):
    def test_init(self):
        self.assertRaises(ValueError, lambda: Frac(1, 0))

    def test_print(self):      # test str() i repr()
        self.assertEqual(str(Frac(1, 2)), '1/2')
        self.assertEqual(str(Frac(3)), '3') 
        self.assertEqual(repr(Frac(1, 2)), 'Frac(1, 2)') 

    def test_add_frac(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(1, 3) + Frac(1, 3), Frac(2, 3))
        self.assertEqual(Frac(1, 3) + Frac(2, 7), Frac(13, 21))
        self.assertEqual(Frac(0, 24) + Frac(0, 24), Frac(0, 24))

    def test_sub_frac(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(1, 3) - Frac(1, 3), Frac(0, 3))
        self.assertEqual(Frac(1, 2) - Frac(2, 7), Frac(3, 14))

    def test_mul_frac(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(1, 3) * Frac(0, 24), Frac(0, 72))
        self.assertEqual(Frac(1, 3) * Frac(3), Frac(1, 1))
        self.assertEqual(Frac(1, 3) * 0, Frac(0, 3))
        self.assertEqual(Frac(1, 3) * -3, Frac(-1, 1))

    def test_rmul_frac(self):
        self.assertEqual(3 * Frac(1, 3), Frac(1, 1))
        self.assertEqual(3 * Frac(3), Frac(9, 1))

    def test_div_frac(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 3), Frac(3, 2))
        self.assertEqual(Frac(1, 2) / 3, Frac(1, 6))
        self.assertRaises(ValueError, lambda: Frac(1, 2) / 0)

    def test_rdiv_frac(self):
        self.assertEqual(i2 / Frac(1, 3), Frac(-9, 1))
        self.assertRaises(ValueError, lambda: Frac(1, 2) / 0)

    def test_eq_frac(self):
        self.assertTrue(Frac(1, 2) == Frac(1, 2))
        self.assertFalse(Frac(1, 2) == Frac(1, 3))

    def test_ne_frac(self):
        self.assertTrue(Frac(1, 2) != Frac(1, 3))
        self.assertFalse(Frac(1, 2) != Frac(1, 2))
        
    def test_lt_frac(self):
        self.assertTrue(Frac(1, 2) > Frac(-1, 2))
        self.assertFalse(Frac(-1, 2) > Frac(1, -2))
 
    def test_le_frac(self):
        self.assertTrue(Frac(1, 2) >= Frac(1, 2))
        
    def test_ge_frac(self):
        self.assertTrue(Frac(1, 2) <= Frac(1, 2))
        
    def test_gt_frac(self):
        self.assertTrue(Frac(-1, 2) < Frac(1, 2))
        self.assertFalse(Frac(-1, 2) < Frac(1, -2))

    def test_pos(self):
        self.assertEqual((+1)*Frac(1, 2), +Frac(1, 2))

    def test_neg(self):        
        self.assertEqual((-1)*Frac(1, 2), -Frac(1, 2))

    def test_invert(self):     
        self.assertEqual(Frac(1, 3), ~Frac(3))
        self.assertFalse(Frac(1, 2) == ~Frac(1, 3))
        self.assertRaises(ValueError, lambda: ~Frac(0, 24))

    def test_float(self):      
        self.assertEqual(float(Frac(1, 2)), 0.5)
        self.assertEqual(float(Frac(0, 24)), 0.0)
        self.assertEqual(float(Frac(1, -2)), -0.5)

    def test_hash(self):
        self.assertTrue(set([2]) == set([2.0]))
        self.assertFalse(set([2]) == set([3]))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy