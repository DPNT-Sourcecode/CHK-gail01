import unittest

from solutions.CHK.checkout_solution import checkout


class CheckoutTests(unittest.TestCase):

    def test_checkout_lowercase(self):
        self.assertEqual(checkout('aAA'), -1)

    def test_checkout_unknown_sku(self):
        self.assertEqual(checkout('z'), -1)

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
            checkout('AAAAAAABBBBBCD'), 455  # 200 + 100 + (2 * 45) + 30 + 20 + 15
        )

    def test_checkout_5a_handling(self):
        self.assertEqual(
            checkout('AAAAAABB'), 295  # 200 + 50 + 45
        )

    def test_checkout_3a_and_5a_plus_singles_handling(self):
        self.assertEqual(
            checkout('AAABAAAAABA'), 425  # 130 + 200 + 50 + 45
        )

    def test_checkout_2e_discount_no_b(self):
        self.assertEqual(
            checkout('EE'), 80
        )

    def test_checkout_2e_discount_with_2b_deal(self):
        # the saving from free item is better than price of 2
        # 2 for 30 versus 2 for 45
        self.assertEqual(
            checkout('EEBB'), 110  # ((40 * 2) + 45) + (-45 + 30)
        )

    def test_checkout_2_2e_discount_with_2b(self):
        self.assertEqual(
            checkout('EEBBEE'), 160  # (40 * 4)
        )

    def test_checkout_2e_b(self):
        self.assertEqual(
            checkout('EEB'), 80  # (40 * 2)
        )

    def test_checkout_3e_b(self):
        self.assertEqual(
            checkout('EEEB'), 120  # (40 * 3)
        )

    def test_checkout_AAAAAEEBAAABB(self):
        self.assertEqual(
            checkout('AAAAAEEBAAABB'), 455  # (200 + 80 + 0 + 130 + 45)
        )

    def test_checkout_FFF(self):
        self.assertEqual(
            checkout('FFF'), 20
        )

    def test_checkout_FF(self):
        self.assertEqual(
            checkout('FF'), 20
        )

    def test_checkout_AAAAAEEBAAABBFFF(self):
        self.assertEqual(
            checkout('AAAAAEEBAAABBFFF'), 475  # (200 + 80 + 0 + 130 + 45 + 20)
        )

    def test_checkout_AAAAAEEBAAABBFFFNNNMRRRQ(self):
        self.assertEqual(
            # (200 + 80 + 0 + 130 + 45 + 20 + 120 + 150)
            checkout('AAAAAEEBAAABBFFFNNNMRRRQ'), 745
        )

    def test_checkout_I(self):
        self.assertEqual(
            checkout('I'), 35
        )

    def test_checkout_J(self):
        self.assertEqual(
            checkout('J'), 60
        )

    def test_checkout_ABCDEFGHIJKLMNOPQRSTUVWXYZ(self):
        self.assertEqual(
            checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 837
        )

    def test_checkout_UUU(self):
        self.assertEqual(
            checkout('UUU'), 120
        )

    def test_checkout_STXYZ(self):
        self.assertEqual(
            checkout('STXYZ'), 82  # 45 + 17 + 20
        )

    def test_checkout_STX(self):
        self.assertEqual(
            checkout('STX'), 45
        )


if __name__ == '__main__':
    unittest.main()
