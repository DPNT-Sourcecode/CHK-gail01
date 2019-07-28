from collections import Counter, namedtuple, defaultdict
from typing import Dict

"""
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+
"""


Deal = namedtuple('Deal', ['sku', 'n_deals'])
DEAL_CONFIG = (
    Deal('A', ((5, 200), (3, 130), (1, 50))),
    Deal('B', ((2, 45), (1, 30))),
    Deal('C', ((1, 20), )),
    Deal('D', ((1, 15), )),
    Deal('E', ((1, 40), )),
)
VALID_SKUS = [d.sku for d in DEAL_CONFIG] + ['E']


def _calculate_multi_item_offer_totals(sku_counts: Dict[str, int]) -> Dict[str, int]:
    deal_sums: Dict[str, int] = defaultdict(int)
    for deal in DEAL_CONFIG:
        total_items_in_order = sku_counts.get(deal.sku)
        if total_items_in_order:
            running_total = 0
            for quotiant, deal_price in deal.n_deals:
                n_count, remainder = divmod(total_items_in_order, quotiant)
                running_total += n_count * deal_price
                total_items_in_order -= (n_count * quotiant)
            deal_sums[deal.sku] = running_total
    return deal_sums


def _calculate_item_adjustment(sku_counts: Dict[str, int]) -> int:
    b_counts = sku_counts.get('B', 0)
    e_counts = sku_counts.get('E', 0)

    two_e_deal_count, _ = divmod(e_counts, 2)
    two_b_deals_count, b_singles = divmod(b_counts, 2)

    # If 2Es, and 2Bs reverse the cost of discounted 2 and add cost of single
    free_item_count = two_e_deal_count
    discounted_price_count = two_b_deals_count
    to_refund = two_e_deal_count - (two_b_deals_count - b_singles)
    print(b_counts, free_item_count, discounted_price_count)
    # 3 1 1
    # if b_singles and free_item_count and not to_refund:
    #     to_discount = two_e_deal_count - (b_counts - two_e_deal_count)
    #     return - (30 * to_discount)
    if two_b_deals_count and free_item_count and discounted_price_count:
        print('refund + discount')
        restore = - (discounted_price_count * 45)
        new_price = (30 * (b_counts - free_item_count))
        adjusted_price = restore + new_price
        return adjusted_price
    elif not two_b_deals_count and b_counts and two_e_deal_count:
        print('discount')
        to_discount = two_e_deal_count - (b_counts - two_e_deal_count)
        return - (30 * to_discount)
    return 0


def checkout(skus: str) -> int:
    if set(skus) - set(VALID_SKUS):
        return -1

    sku_counts = Counter(skus)
    multi_offer_totals = _calculate_multi_item_offer_totals(sku_counts)

    preliminary_total = sum([v for v in multi_offer_totals.values()])

    adjusted_free_b = _calculate_item_adjustment(sku_counts)
    print('----------')
    return preliminary_total + adjusted_free_b







