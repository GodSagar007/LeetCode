from typing import List
import pytest

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def simulate(houses):
            prev, curr = 0, 0
            for amount in houses:
                prev, curr = curr, max(curr, prev + amount)
            return curr
        return max(simulate(nums[:-1]), simulate(nums[1:]))

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], 0),                       # No houses
        ([1], 1),                      # Single house
        ([2, 3, 2], 3),                # Rob house 1 or 2
        ([1, 2, 3, 1], 4),             # Rob house 2 and 4
        ([0, 0, 0], 0),                # All zero
        ([5, 1, 1, 5], 10),            # Rob house 1 and 4
        ([1, 3, 1, 3, 100], 103),      # Rob house 2 and 5
        ([200, 3, 140, 20, 10], 340),  # Rob house 1 and 3
        ([2, 2, 4, 3, 2, 5], 10),      # Rob 1, 4, 6
        ([6, 7, 1, 30, 8, 2, 4], 41),  # Larger example
    ]
)
def test_rob(nums, expected):
    assert Solution().rob(nums) == expected
