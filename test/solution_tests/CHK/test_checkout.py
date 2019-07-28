import unittest

from solutions.CHK.checkout_solution import checkout


class CheckoutTests(unittest.TestCase):
    def test_checkout(self):
        checkout('AAABBCD')
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
