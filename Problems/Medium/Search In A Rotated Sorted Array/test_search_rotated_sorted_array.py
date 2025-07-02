import pytest

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:  # Left half is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:  # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


@pytest.mark.parametrize("nums, target, expected", [
    # Classic cases
    ([4,5,6,7,0,1,2], 0, 4),
    ([4,5,6,7,0,1,2], 3, -1),
    ([1], 0, -1),
    ([1], 1, 0),

    # Fully sorted (not rotated)
    ([1,2,3,4,5,6], 4, 3),

    # Rotation at middle
    ([6,7,1,2,3,4,5], 2, 3),

    # Target is first or last
    ([5,1,3], 5, 0),
    ([5,1,3], 3, 2),

    # Array with two elements
    ([1,3], 3, 1),
    ([3,1], 1, 1),
    ([3,1], 2, -1),

    # Edge case: Empty array
    ([], 1, -1),

    # Duplicates not expected in LeetCode 33, but test anyway
    ([2,2,2,3,4,2], 3, 3),
])
def test_search(nums, target, expected):
    sol = Solution()
    assert sol.search(nums, target) == expected
