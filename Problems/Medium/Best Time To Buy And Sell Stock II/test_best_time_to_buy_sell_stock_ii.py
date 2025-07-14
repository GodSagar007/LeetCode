import pytest
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

@pytest.mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 7),       # Buy at 1→5 (4), buy at 3→6 (3) => 7
    ([1, 2, 3, 4, 5], 4),          # Ascending → max profit = 4
    ([7, 6, 4, 3, 1], 0),          # Descending → no profit
    ([1], 0),                      # Single element → no transactions
    ([2, 1, 2, 1, 2], 2),          # Two upswings → profit = 2
    ([2, 4, 1, 7], 8),             # 2→4 (2), 1→7 (6) => 8
    ([3, 3, 5, 0, 0, 3, 1, 4], 8), # 3→5 (2), 0→3 (3), 1→4 (3) => 8
    ([2, 2, 2, 2], 0),             # No price movement → profit = 0
])
def test_max_profit(prices: List[int], expected: int):
    sol = Solution()
    assert sol.maxProfit(prices) == expected
