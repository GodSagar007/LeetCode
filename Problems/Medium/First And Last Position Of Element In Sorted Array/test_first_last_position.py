from typing import List
import pytest

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, -1

        def findLeft():
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        def findRight():
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high

        left = findLeft()
        right = findRight()

        if left <= right and left < len(nums) and nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]


@pytest.mark.parametrize("nums, target, expected", [
    # Typical case
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    # Target not present
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    # Single element - match
    ([2], 2, [0, 0]),
    # Single element - no match
    ([2], 3, [-1, -1]),
    # All same target
    ([4, 4, 4, 4, 4], 4, [0, 4]),
    # Target at beginning
    ([2, 3, 3, 4, 5], 2, [0, 0]),
    # Target at end
    ([1, 1, 2, 3, 3], 3, [3, 4]),
    # Empty array
    ([], 1, [-1, -1]),
    # All numbers less than target
    ([1, 2, 3], 5, [-1, -1]),
    # All numbers greater than target
    ([10, 20, 30], 5, [-1, -1]),
    # Mixed numbers with one match
    ([1, 2, 3, 5, 6, 8, 9], 5, [3, 3]),
    # Target appears twice
    ([1, 3, 3, 5, 7], 3, [1, 2]),
])
def test_search_range(nums: List[int], target: int, expected: List[int]):
    s = Solution()
    assert s.searchRange(nums, target) == expected
