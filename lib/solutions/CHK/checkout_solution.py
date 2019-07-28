import string
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


PRICE_LOOKUP = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}

Deal = namedtuple('Deal', ['sku', 'n_deals'])
DEAL_CONFIG = (
    Deal('A', ((5, 200), (3, 130), (1, 50))),
    Deal('B', ((2, 45), (1, 30))),
    Deal('C', ((1, 20), )),
    Deal('D', ((1, 15), )),
    Deal('E', ((1, 40), )),
)


def _calculate_multi_item_offer_totals(sku_counts: Dict[str, int]) -> Dict[str, int]:
    deal_sums = defaultdict(int)
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


# TODO Handle discounting an item (if exists in skus) if multi-deal available

def checkout(skus: str) -> int:
    # Should only contain uppercases Letters in input
    if set(skus).intersection(set(string.ascii_lowercase)):
        return -1
    if set(skus) - set(PRICE_LOOKUP.keys()):
        return -1

    sku_counts = Counter(skus)
    multi_offer_totals = _calculate_multi_item_offer_totals(sku_counts)

    return sum([v for v in multi_offer_totals.values()])

