from typing import List
import pytest

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = 1
        output = [0] * n
        for i in range(n):
            output[i] = pre
            pre *= nums[i]
        post = 1
        for i in reversed(range(n)):
            output[i] *= post
            post *= nums[i]
        return output


@pytest.mark.parametrize("nums, expected", [
    # Basic case
    ([1, 2, 3, 4], [24, 12, 8, 6]),

    # Contains a zero
    ([1, 2, 0, 4], [0, 0, 8, 0]),

    # Contains two zeros
    ([0, 2, 0, 4], [0, 0, 0, 0]),

    # All ones
    ([1, 1, 1, 1], [1, 1, 1, 1]),

    # Negative numbers
    ([2, -3, 4], [-12, 8, -6]),

    # All same number
    ([5, 5, 5, 5], [125, 125, 125, 125]),

    # Mix of positive and negative
    ([1, -1, 2, -2], [4, -4, 2, -2]),

    # Two elements
    ([3, 4], [4, 3]),

    # One element (edge case)
    ([42], [1]),  # As per LeetCode, assume this won't be run in production unless specified

    # Large numbers
    ([1000, 100, 10, 1], [1000, 10000, 100000, 1000000])
])
def test_product_except_self(nums: List[int], expected: List[int]):
    s = Solution()
    assert s.productExceptSelf(nums) == expected
