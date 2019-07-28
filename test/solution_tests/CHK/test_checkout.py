import unittest

from solutions.CHK.checkout_solution import checkout


class CheckoutTests(unittest.TestCase):
    def test_checkout(self):
        checkout('AAABBCD')
        self.assertEqual(True, False)

    def test_checkout_lowercase(self):
        self.assertEqual(checkout('aAA'), -1)

    def test_checkout_unknown_sku(self):
        self.assertEqual(checkout('Z'), -1)


if __name__ == '__main__':
    unittest.main()

