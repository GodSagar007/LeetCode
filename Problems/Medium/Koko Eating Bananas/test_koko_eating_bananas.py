import pytest
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            k = low + (high - low) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                ans = min(ans, k)
                high = k - 1
            else:
                low = k + 1

        return ans

sol = Solution()

@pytest.mark.parametrize(
    "piles, h, expected",
    [
        ([3,6,7,11], 8, 4),         # Can eat in 8 hours with speed 4
        ([30,11,23,4,20], 5, 30),  # Must eat fastest to meet 5 hours
        ([30,11,23,4,20], 6, 23),  # Slightly more time, slightly slower speed
        ([1], 1, 1),               # Single pile, 1 hour
        ([1000000000], 2, 500000000), # Large number, two hours
        ([1,1,1,1], 4, 1),         # All small piles, minimal speed needed
        ([10, 10, 10, 10], 4, 10), # Each pile must be eaten in one hour
        ([10, 10, 10, 10], 8, 5),  # Can split piles across hours
        ([1000000, 1000000], 3, 1000000), # High precision needed
    ]
)
def test_min_eating_speed(piles, h, expected):
    assert sol.minEatingSpeed(piles, h) == expected
