import unittest


class MinOfThreeVarsTestCase(unittest.TestCase):
    def test_min_a(self):
        self.assertEqual(min_of_three_vars(1, 2, 3), 1)
    
    def test_min_b(self):
        self.assertEqual(min_of_three_vars(2, 1, 3), 1)

    def test_min_c(self):
        self.assertEqual(min_of_three_vars(3, 2, 1), 1)


class ToUpperTestCase(unittest.TestCase):
    def test_to_upper(self):
        self.assertEqual(to_upper_text('blabla'), 'BLABLA')


class ToUpperTestCase(unittest.TestCase):
    def test_is_divided(self):
        self.assertEqual(is_divided(24), True)

    def test_is_not_divided(self):
        self.assertEqual(is_divided(23), False)


def min_of_three_vars(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c


def to_upper_text(text):
    return text.upper()


def is_divided(a):
    if a % 12 == 0:
        return True
    else:
        return False
