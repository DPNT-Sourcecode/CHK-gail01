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
        print('test_checkout_2e_b')
        self.assertEqual(
            checkout('EEB'), 80  # (40 * 2)
        )
        print('------')

    # def test_checkout_3e_b(self):
    #     self.assertEqual(
    #         checkout('EEEB'), 120  # (40 * 3)
    #     )
    #
    # def test_checkout_AAAAAEEBAAABB(self):
    #     self.assertEqual(
    #         checkout('AAAAAEEBAAABB'), 455
    #     )


if __name__ == '__main__':
    unittest.main()




