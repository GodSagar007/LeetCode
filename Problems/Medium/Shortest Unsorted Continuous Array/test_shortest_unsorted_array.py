from typing import List
import pytest

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # Find the first out-of-order index from the left
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1
        if left == n - 1:
            return 0  # Already sorted

        # Find the first out-of-order index from the right
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        # Find min and max within the unsorted subarray
        min_val = min(nums[left:right + 1])
        max_val = max(nums[left:right + 1])

        # Expand left and right to include any out-of-bound elements
        while left > 0 and nums[left - 1] > min_val:
            left -= 1
        while right < n - 1 and nums[right + 1] < max_val:
            right += 1

        return right - left + 1

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 6, 4, 8, 10, 9, 15], 5),       # Normal case
        ([1, 2, 3, 4], 0),                  # Already sorted
        ([1], 0),                           # Single element
        ([1, 3, 2, 2, 2], 4),               # Mid unsorted
        ([1, 2, 3, 3, 3], 0),               # Duplicates, sorted
        ([1, 2, 4, 5, 3], 3),               # Disorder at the end
        ([5, 4, 3, 2, 1], 5),               # Fully reversed
        ([1, 3, 5, 4, 2, 6, 7], 5),         # Needs expansion of bounds
        ([1, 2, 3, 10, 9, 8, 15], 3),       # Short subarray in middle
        ([1, 2, 3, 3, 2, 2], 4),            # Decreasing part at end
        ([1, 2, 3, 5, 4], 2),               # Just two elements swapped
    ]
)
def test_find_unsorted_subarray(nums, expected):
    assert Solution().findUnsortedSubarray(nums) == expected
