import pytest
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        ans = high

        def calcDays(capacity):
            d = 1
            curr = 0
            for weight in weights:
                if curr + weight > capacity:
                    curr = 0
                    d += 1
                curr += weight
            return d

        while low <= high:
            mid = (low + high) // 2
            needed = calcDays(mid)
            if needed <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

@pytest.mark.parametrize("weights, days, expected", [
    ([1,2,3,4,5,6,7,8,9,10], 5, 15),     # Balanced split over 5 days
    ([3,2,2,4,1,4], 3, 6),               # Multiple valid splits, 6 is minimal capacity
    ([1,2,3,1,1], 4, 3),                 # Spread out as much as possible
    ([10], 1, 10),                       # One package only
    ([1]*100, 10, 10),                   # Uniform weights, divide evenly
    ([5,5,5,5,5,5,5,5,5,5], 2, 25),      # Needs 2 days → half in each
    ([7,2,5,10,8], 2, 18),              # Min capacity = 18 for 2 days
    ([1,2,3,4,5], 1, 15),                # One day → sum of all weights
    ([1,2,3,4,5], 5, 5),                 # One package per day
])
def test_ship_within_days(weights: List[int], days: int, expected: int):
    sol = Solution()
    assert sol.shipWithinDays(weights, days) == expected
