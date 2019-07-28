

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
import string

LOOKUP = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    # Should only contain uppercases Letters in input
    if set(skus).intersection(set(string.ascii_lowercase)):
        return -1
    if set(skus)
    return -1


