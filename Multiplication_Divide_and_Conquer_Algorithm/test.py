import unittest
from multiplication import multi
import random


class Test_multiplication(unittest.TestCase):
    def test_mult1(self):
        self.assertEqual(multi(0, 2233), 0)
        self.assertEqual(multi(2332, 0), 0)
        self.assertEqual(multi(1, 2333), 2333)
        self.assertEqual(multi(2333, 1), 2333)

    def test_mult2(self):
        self.assertEqual(multi(2, 22), 44)
        self.assertEqual(multi(10, 60), 600)
        self.assertEqual(multi(44, 2), 88)
        self.assertEqual(multi(22, 22), 484)

    def test_mult3(self):
        num_1 = random.randint(0, 100)
        num_2 = random.randint(0, 100)
        self.assertEqual(multi(num_1, num_2), num_1 * num_2)

    def test_mult4(self):
        self.assertEqual(multi(123, 456), 56088)
        self.assertEqual(multi(9999, 1111), 11108889)
        self.assertEqual(multi(123456, 7890), 974067840)
        self.assertEqual(multi(98765, 4321), 426763565)

    def test_mult5(self):
        self.assertEqual(multi(1, 1), 1)
        self.assertEqual(multi(1, 2), 2)
        self.assertEqual(multi(2, 2), 4)
        self.assertEqual(multi(9, 9), 81)


if __name__ == "__main__":
    unittest.main()
