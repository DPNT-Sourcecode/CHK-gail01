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
VALID_SKUS = [d.sku for d in DEAL_CONFIG]


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


def _calculate_free_items_discount(sku_counts: Dict[str, int]) -> int:
    b_counts = sku_counts.get('B', 0)
    e_counts = sku_counts.get('E', 0)

    two_e_deal_count, _ = divmod(e_counts, 2)
    two_b_deals_count, b_singles = divmod(b_counts, 2)
    print('----')
    print('2e_deals_count, ', two_e_deal_count)
    print('b_singles, ', b_singles)
    print(two_e_deal_count - b_singles)
    print((two_e_deal_count - b_singles) * 30)
    print('----')
    mult_2, remainder = divmod(two_e_deal_count, 2)
    # if b deals are a multiple of 2 remove that many from qualify 2e
    to_remove = ((two_b_deals_count * 2) - mult_2) * 45
    if b_singles and not two_b_deals_count:
        to_remove += (b_singles - remainder) * 30 if (b_singles - remainder) > 0 else 0
    return to_remove


def checkout(skus: str) -> int:
    if set(skus) - set(VALID_SKUS):
        return -1

    sku_counts = Counter(skus)
    multi_offer_totals = _calculate_multi_item_offer_totals(sku_counts)

    print('n_totals_data')
    print([v for v in multi_offer_totals.values()])
    preliminary_total = sum([v for v in multi_offer_totals.values()])

    # TODO Handle discounting an item (if exists in skus) if multi-deal available
    # ??? Always better to ignore free item if multi exists for that SKU?

    discount = _calculate_free_items_discount(sku_counts)
    print('discount', discount)
    return preliminary_total - discount

