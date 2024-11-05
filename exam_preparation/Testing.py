import unittest


def simple_sum(a, b):
    return a + b


class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(simple_sum(3, 5), 8)
