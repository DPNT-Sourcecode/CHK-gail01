import unittest

from solutions.CHK.checkout_solution import checkout


class CheckoutTests(unittest.TestCase):

    def test_checkout_lowercase(self):
        self.assertEqual(checkout('aAA'), -1)

    def test_checkout_unknown_sku(self):
        self.assertEqual(checkout('Z'), -1)

    def test_checkout_illegal_chars(self):
        self.assertEqual(checkout('%'), -1)

    def test_basic_checkout_no_deals(self):
        self.assertEqual(
            checkout('AABCCCD'), 205  # (50 * 2) + 30 + (20 * 3) + 15
        )

    def test_checkout_with_deals(self):
        self.assertEqual(
            checkout('AAABBCD'), 210  # 130 + 45 + 20 + 15
        )

    def test_checkout_with_multiple_deals(self):
        self.assertEqual(
            checkout('AAAAAAABBBBBCD'), 465  # (2 * 130) + 50 + (2 * 45) + 30 + 20 + 15
        )

    def test_checkout_5a_handling(self):
        self.assertEqual(
            checkout('AAAAAABB'), 245  # 200 + 45
        )

    def test_checkout_3a_and_5a_plus_singles_handling(self):
        self.assertEqual(
            checkout('AAABAAAAABA'),  # 130 + 200 + 50 + 45
        )


if __name__ == '__main__':
    unittest.main()



