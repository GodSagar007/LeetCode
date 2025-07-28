import pytest
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        ans = 0
        window_sum = 0

        for r in range(len(nums)):
            window_sum += nums[r]
            while nums[r] * (r - l + 1) - window_sum > k:
                window_sum -= nums[l]
                l += 1
            ans = max(ans, r - l + 1)

        return ans

@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 4], 5, 3),                   # all can be made 4
    ([1, 4, 8, 13], 5, 2),              # best is [4, 8] -> both 8
    ([3, 9, 6], 2, 1),                  # not enough k to equalize
    ([1, 2, 2, 2, 2], 0, 4),            # already same, no ops needed
    ([3, 3, 3, 3], 3, 4),               # already same, all same
    ([1], 100, 1),                      # single element
    ([3, 3, 3, 4, 4, 4, 5], 3, 5),      # multiple small ops
    ([1, 2, 3, 4, 5], 10, 5),           # can equalize all
])
def test_max_frequency(nums: List[int], k: int, expected: int):
    assert Solution().maxFrequency(nums, k) == expected
