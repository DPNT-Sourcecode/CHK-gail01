import string
from collections import Counter

"""
Our price table and offers:
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
"""
PRICE_LOOKUP = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

DEAL_LOOKUP = {
    ('A', 3): 130,
    ('B', 2): 45
}


def checkout(skus: str) -> int:
    # Should only contain uppercases Letters in input
    if set(skus).intersection(set(string.ascii_lowercase)):
        return -1
    if set(skus) - set(PRICE_LOOKUP.keys()):
        return -1

    sku_counts = Counter(skus)
    a_deal_count, a_singles = divmod(sku_counts.pop('A', 0), 3)
    a_total = (a_deal_count * 130) + (a_singles * 50)
    b_deal_count, b_singles = divmod(sku_counts.pop('B', 0), 3)
    b_total = (b_deal_count * 130) + (b_singles * 50)
    rest = sum([PRICE_LOOKUP[s] for s in sku_counts.keys()])

    return a_total + b_total + rest
