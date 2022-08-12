from unittest import TestCase, main
from fnum import fibo, facto


class TestFnum(TestCase):
    def test_facto_neg(self):
        with self.assertRaises(OverflowError):
            facto(-1)

    def test_fibo_neg(self):
        with self.assertRaises(OverflowError):
            fibo(-2)

    def test_facto_6(self):
        self.assertEqual(facto(6), 720)

    def test_fibo_10(self):
        self.assertEqual(fibo(10), 55)

    def test_fibo_instance(self):
        self.assertIsInstance(fibo(6), int)

    def test_facto_instance(self):
        self.assertIsInstance(facto(7), int)


if __name__ == "__main__":
    main()
