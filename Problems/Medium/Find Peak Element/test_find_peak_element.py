import pytest
from typing import List

# Your peak-finding implementation
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            mid = l + (h - l) // 2
            if nums[mid] > nums[mid + 1]:
                h = mid
            else:
                l = mid + 1
        return h

# Pytest test cases
@pytest.mark.parametrize(
    "nums, expected_peaks",
    [
        # Single element (trivial peak)
        ([1], [0]),

        # Two elements
        ([1, 2], [1]),
        ([2, 1], [0]),

        # Peak in middle
        ([1, 3, 2], [1]),
        ([1, 2, 3, 1], [2]),
        ([1, 4, 2, 3, 1], [1, 3]),  # multiple possible peaks

        # Flat areas with edge peak
        ([1, 1, 1, 1, 2], [4]),
        ([3, 1, 1, 1, 1], [0]),

        # Strictly increasing / decreasing
        ([1, 2, 3, 4, 5], [4]),
        ([5, 4, 3, 2, 1], [0]),

        # Multiple peaks
        ([1, 3, 2, 4, 1], [1, 3]),

        # Large flat area with peak
        ([0] * 100 + [10] + [0] * 100, [100]),
    ]
)
def test_find_peak(nums, expected_peaks):
    index = Solution().findPeakElement(nums)
    assert index in expected_peaks
    # Also verify peak property
    left = nums[index - 1] if index > 0 else float('-inf')
    right = nums[index + 1] if index < len(nums) - 1 else float('-inf')
    assert nums[index] > left and nums[index] > right
