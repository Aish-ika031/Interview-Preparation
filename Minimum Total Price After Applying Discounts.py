from typing import List

class Solution:
    def minimumTotal(self, prices: List[int], discounts: List[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        total = 0.0

        for i, price in enumerate(prices):
            if i < len(discounts):
                total += price * (100 - discounts[i]) / 100
            else:
                total += price

        return total
