import string
from collections import Counter

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

# TODO Handle various offers on same item
# TODO Handle discounting an item (if exists in skus) if multi-deal available

PRICE_LOOKUP = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

DEAL_CONFIG = (
    ('A', 3, 130, 50),
    ('B', 2, 45, 30),
)  # TODO Convert to NamedTuple or similar?


def checkout(skus: str) -> int:
    # Should only contain uppercases Letters in input
    if set(skus).intersection(set(string.ascii_lowercase)):
        return -1
    if set(skus) - set(PRICE_LOOKUP.keys()):
        return -1

    sku_counts = Counter(skus)
    multi_offers_total = 0
    for item_code, deal_num, deal_cost, normal_cost in DEAL_CONFIG:
        item_deal_count, item_singles = divmod(sku_counts.pop(item_code, 0), deal_num)
        multi_offers_total += (item_deal_count * deal_cost) + (item_singles * normal_cost)

    rest = sum([PRICE_LOOKUP[s] * c for s, c in sku_counts.items()])
    return multi_offers_total + rest





