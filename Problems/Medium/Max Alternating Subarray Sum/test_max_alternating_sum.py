from typing import List
import pytest

class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        max_sum = pos = neg = float('-inf')
        for num in nums:
            pos, neg = max(neg + num, num), pos - num
            max_sum = max(max_sum, pos, neg)
        return max_sum

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, -1, 1, 2], 5),              # best subarray: [3, -1, 1]
        ([1], 1),                        # single element
        ([1, 2], 1),                     # 1 or 2 -> best is 1
        ([2, 1], 2),                     # just 2
        ([1, 2, 3, 4], 4),               # 4 is best alone
        ([4, 3, 2, 1], 4),               # same
        ([1, -2, 3, -4, 5], 11),         # 1 - (-2) + 3 - (-4) + 5 = 15 (but best *contiguous* is 11)
        ([-1, -2, -3], -1),              # best is -1
        ([5, -1, 3, -2, 4, -3], 14),     # 5 - (-1) + 3 - (-2) + 4 = 14
        ([10, -10, 10, -10], 30),        # 10 - (-10) + 10 = 30
        ([1000, -1000], 2000),           # 1000 - (-1000) = 2000
    ]
)
def test_maximum_alternating_subarray_sum(nums, expected):
    assert Solution().maximumAlternatingSubarraySum(nums) == expected
