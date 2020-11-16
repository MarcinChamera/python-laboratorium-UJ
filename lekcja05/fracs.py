def gcd(a, b):
    r= a % b
    while r:
        a = b
        b = r
        r = a % b
    return b


def polish(num, den):
    if num == 0:
        return [0, den]
    gcd_res = gcd(num, den)
    num /= gcd_res
    den /= gcd_res
    return [num, den]


def add_frac(frac1, frac2):        # frac1 + frac2
    if frac1[1] == frac2[1]:
        numerator = frac1[0] + frac2[0]
        denumerator = frac1[1]
    else:
        numerator = (frac1[0] * frac2[1]) + (frac2[0] * frac1[1])
        denumerator = frac1[1] * frac2[1]
    return polish(numerator, denumerator)


def sub_frac(frac1, frac2):        # frac1 - frac2
    if frac1[1] == frac2[1]:
        numerator = frac1[0] - frac2[0]
        denumerator = frac1[1]
    else:
        numerator = (frac1[0] * frac2[1]) - (frac2[0] * frac1[1])
        denumerator = frac1[1] * frac2[1]
    return polish(numerator, denumerator)



def mul_frac(frac1, frac2):        # frac1 * frac2
    numerator = frac1[0] * frac2[0]
    denumerator = frac1[1] * frac2[1]
    return polish(numerator, denumerator)
    

def div_frac(frac1, frac2):        # frac1 / frac2
    numerator = frac1[0] * frac2[1] 
    denumerator = frac1[1] * frac2[0]
    return polish(numerator, denumerator)


def is_positive(frac):             # bool, czy dodatni
    return (frac[0] / frac[1]) > 0


def is_zero(frac):                 # bool, typu [0, x]
    return frac[0] == 0


def frac_sign(frac):
    if self.is_positive(frac):
        return 1
    if self.is_zero(frac):
        return 0
    return -1


def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    f1, f2 = frac2float(frac1), frac2float(frac2)
    if f1 == f2 == 0:
        return 0
    if f1 > f2:
        return -1
    if f1 < f2:
        return 1


def frac2float(frac):              # konwersja do float
    return frac[0] / frac[1]


f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznaczność)
f5 = [0, 2]                   # zero (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 3], [1, 3]), [2, 3])
        self.assertEqual(add_frac([1, 3], [2, 7]), [13, 21])
        self.assertEqual(add_frac([5, 24], [11, 24]), [2, 3])
        self.assertEqual(add_frac([0, 24], [0, 24]), [0, 24])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([11, 24], [5, 24]), [1, 4])
        self.assertEqual(sub_frac([1, 3], [1, 3]), [0, 3])
        self.assertEqual(sub_frac([1, 3], [2, 7]), [1, 21])


    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([0, 2], [1, 3]), [0, 6])
        self.assertEqual(mul_frac([1, 3], [3, 1]), [1, 1])
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])


    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])


    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([1, -2]), False)
        self.assertEqual(is_positive([-1, -2]), True)


    def test_is_zero(self): 
        self.assertEqual(is_zero([1, 2]), False)
        self.assertEqual(is_zero([0, 2]), True)


    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), -1)
        self.assertEqual(cmp_frac([0, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([-1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, -2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 2], [-1, 3]), -1)
        self.assertEqual(cmp_frac([1, 2], [1, -3]), -1)
        self.assertEqual(cmp_frac([-1, 2], [-1, 3]), 1)
        self.assertEqual(cmp_frac([-1, 2], [1, -3]), 1)
        self.assertEqual(cmp_frac([1, -2], [1, -3]), 1)
        self.assertEqual(cmp_frac([1, -2], [-1, 3]), 1)
        self.assertEqual(cmp_frac([0, 2], [0, 3]), 0)


    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)


    def tearDown(self): pass
if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy