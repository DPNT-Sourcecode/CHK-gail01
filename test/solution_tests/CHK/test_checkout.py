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

    def test_basic_checkout_no_deals(self):
        self.assertEqual(
            checkout('AABCCCD'), 205  # (50 * 2) + 30 + (20 * 3) + 15
        )

    def test_checkout_with_deals(self):
        self.assertEqual(
            checkout('AAABBCD'), 130 + 45 + 20 + 15
        )


if __name__ == '__main__':
    unittest.main()


