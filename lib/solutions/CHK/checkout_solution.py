import string

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
    'D': 15
}


def checkout(skus: str) -> int:
    # Should only contain uppercases Letters in input
    if set(skus).intersection(set(string.ascii_lowercase)):
        return -1
    if set(skus) - set(PRICE_LOOKUP.keys()):
        return -1
    try:
        return sum([PRICE_LOOKUP[s] for s in skus])
    except IndexError:
        return -1




