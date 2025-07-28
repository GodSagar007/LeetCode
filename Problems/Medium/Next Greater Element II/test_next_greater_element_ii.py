from typing import List
import pytest

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in reversed(range(2 * n - 1)):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if stack and i < n:
                result[i] = stack[-1]
            stack.append(nums[i % n])

        return result

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 1], [2, -1, 2]),               # Wrap-around needed
        ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),   # Increasing with a dip at end
        ([5, 4, 3, 2, 1], [-1, 5, 5, 5, 5]),   # Descending, wraps to first element
        ([1, 1, 1, 1], [-1, -1, -1, -1]),      # All equal
        ([2, 1, 2, 4, 3], [4, 2, 4, -1, 4]),   # Mix of increasing and decreasing
        ([100, 1, 11, 1, 120, 111, 123, 1, -1, -100], [120, 11, 120, 120, 123, 123, -1, 100, 100, 100]),
        ([3], [-1]),                          # Single element
    ]
)
def test_next_greater_elements(nums, expected):
    assert Solution().nextGreaterElements(nums) == expected
