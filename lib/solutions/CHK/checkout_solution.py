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
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+
"""


Deal = namedtuple('Deal', ['sku', 'n_deals'])
DEAL_CONFIG = (
    Deal('A', ((5, 200), (3, 130), (1, 50))),
    Deal('B', ((2, 45), (1, 30))),
    Deal('C', ((1, 20), )),
    Deal('D', ((1, 15), )),
    Deal('E', ((1, 40), )),
    Deal('F', ((3, 20), (2, 20), (1, 10))),
    Deal('G', ((1, 20), )),
    Deal('H', ((10, 80), (5, 45), (1, 10))),
    Deal('I', ((1, 35), )),
    Deal('J', ((1, 60), )),
    Deal('K', ((2, 150), (1, 80))),
    Deal('L', ((1, 90), )),
    Deal('M', ((1, 15), )),
    Deal('N', ((1, 40), )),
    Deal('O', ((1, 10), )),
    Deal('P', ((5, 200), (1, 50))),
    Deal('Q', ((3, 80), (1, 30))),
    Deal('R', ((1, 50), )),
    Deal('S', ((1, 30), )),
    Deal('T', ((1, 20), )),
    Deal('U', ((4, 120), (3, 120), (2, 80), (1, 40))),
    Deal('V', ((3, 130), (2, 90), (1, 50))),
    Deal('W', ((1, 20), )),
    Deal('X', ((1, 90), )),
    Deal('Y', ((1, 10), )),
    Deal('Z', ((1, 50), )),
)
VALID_SKUS = [d.sku for d in DEAL_CONFIG]
DEAL_LOOKUP = {d.sku: d for d in DEAL_CONFIG}
ADJUSTMENT_LOOKUP = {
    'E': (2, 2, 45, 30),
    'N': (3, 1, 0, 15),
    'R': (3, 3, 80, 30)
}


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


def _calculate_item_adjustment(main_sku: str, free_sku: str, sku_counts: Dict[str, int]) -> int:
    main_item_deal_group, second_item_deal_group, refund, discount = ADJUSTMENT_LOOKUP[main_sku]

    main_item_count = sku_counts.get(main_sku, 0)
    second_item_count = sku_counts.get(free_sku, 0)

    main_deal_count, _ = divmod(main_item_count, main_item_deal_group)
    if second_item_deal_group > 1:
        secondary_deal_count, secondary_singles = divmod(second_item_count, second_item_deal_group)
    else:
        secondary_deal_count, secondary_singles = 0, second_item_count

    free_item_count = main_deal_count
    to_refund = main_deal_count - (main_deal_count - (secondary_deal_count - secondary_singles)) if secondary_deal_count else 0

    # If user paid full price on a discounted now free time, refund deal and apply cost of reduced item number
    if refund and secondary_deal_count and free_item_count and not secondary_singles:
        restore = - (to_refund * refund)
        new_price = (discount * (second_item_count - free_item_count))
        adjusted_price = restore + new_price
        return adjusted_price
    # if user has only single secondary in order then discount with number of 2e
    elif secondary_singles and main_deal_count:
        to_discount = main_deal_count - (secondary_singles - main_deal_count)
        return - (discount * to_discount)
    return 0


def checkout(skus: str) -> int:
    if set(skus) - set(VALID_SKUS):
        return -1

    sku_counts = Counter(skus)
    multi_offer_totals = _calculate_multi_item_offer_totals(sku_counts)

    preliminary_total = sum([v for v in multi_offer_totals.values()])
    adjusted_free_b = _calculate_item_adjustment('E', 'B', sku_counts)
    adjusted_free_m = _calculate_item_adjustment('N', 'M', sku_counts)
    adjusted_free_q = _calculate_item_adjustment('R', 'Q', sku_counts)
    return preliminary_total + adjusted_free_b + adjusted_free_m + adjusted_free_q








