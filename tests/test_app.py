import unittest


def add(a, b):
    return a + b


class TestApp(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 6)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
