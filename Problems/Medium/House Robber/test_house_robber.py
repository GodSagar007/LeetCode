from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]


# ---------------------- Pytest Tests ----------------------

import pytest

@pytest.mark.parametrize(
    "nums, expected",
    [
        # Base cases
        ([1], 1),
        ([2, 3], 3),
        ([3, 2, 3], 6),

        # Typical case
        ([2, 7, 9, 3, 1], 12),  # rob 2 + 9 + 1
        ([1, 2, 3, 1], 4),      # rob 1 + 3

        # All houses with same amount
        ([5, 5, 5, 5, 5], 15),  # rob 5+5+5

        # Increasing amounts
        ([1, 2, 3, 4, 5], 9),   # rob 1+3+5

        # Decreasing amounts
        ([5, 4, 3, 2, 1], 9),   # rob 5+3+1

        # Alternating pattern
        ([2, 1, 1, 2], 4),      # rob 2 + 2

        # Large numbers
        ([100, 1, 1, 100], 200),

        # Two houses, second one larger
        ([1, 100], 100),

        # Edge case: zeros
        ([0, 0, 0, 0], 0),

        # Edge case: max at beginning and end
        ([10, 1, 1, 10], 20),
    ]
)
def test_rob(nums, expected):
    sol = Solution()
    assert sol.rob(nums) == expected
