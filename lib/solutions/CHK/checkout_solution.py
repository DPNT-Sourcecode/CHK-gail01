import string
from collections import Counter, namedtuple, defaultdict

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
    'E': 40,
}

DEAL_CONFIG = (
    ('A', 3, 130, 50),
    ('A', 5, 200, 50),
    ('B', 2, 45, 30),
)


def checkout(skus: str) -> int:
    # Should only contain uppercases Letters in input
    if set(skus).intersection(set(string.ascii_lowercase)):
        return -1
    if set(skus) - set(PRICE_LOOKUP.keys()):
        return -1

    sku_counts = Counter(skus)
    mutli_offer_totals = defaultdict(list)
    for item_code, deal_num, deal_cost, normal_cost in DEAL_CONFIG:
        item_deal_count, item_singles = divmod(sku_counts.pop(item_code, 0), deal_num)
        mutli_offer_totals[item_code].append((item_deal_count * deal_cost) + (item_singles * normal_cost))

    rest = sum([PRICE_LOOKUP[s] * c for s, c in sku_counts.items()])
    return [min(v) for v in mutli_offer_totals.values()] + rest


