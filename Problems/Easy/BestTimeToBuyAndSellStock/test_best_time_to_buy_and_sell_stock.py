import pytest
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(minPrice, price)

        return maxProfit

sol = Solution()

@pytest.mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 5),              # Buy at 1, sell at 6
    ([7, 6, 4, 3, 1], 0),                 # Prices decreasing → no profit
    ([1, 2, 3, 4, 5], 4),                 # Increasing sequence
    ([1], 0),                             # Only one price → no transaction
    ([3, 3, 3, 3], 0),                    # All values same
    ([2, 4, 1], 2),                       # Buy at 2, sell at 4
    ([5, 11, 3, 50, 60, 90], 87),         # Buy at 3, sell at 90
    ([9, 8, 6, 2, 5, 3, 8], 6),           # Buy at 2, sell at 8
    ([100, 180, 260, 310, 40, 535, 695], 655),  # Buy at 40, sell at 695
    ([2, 1, 2, 1, 2, 1, 2], 1),           # Multiple buy-sell cycles, max one transaction
    ([1, 1000], 999),                    # Large jump
    ([1000, 1], 0),                      # Large drop
])
def test_max_profit(prices, expected):
    assert sol.maxProfit(prices) == expected
