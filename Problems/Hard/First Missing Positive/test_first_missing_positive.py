from typing import List
import pytest

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([1, 2, 3], 4),
        ([-1, -2, -3], 1),
        ([7, 8, 9, 11, 12], 1),
        ([1, 1, 0, -1, -2], 2),
        ([2, 1, 4], 3),
        ([1000], 1),
        ([3, 4, 1, 2], 5),
        ([], 1),
    ]
)
def test_firstMissingPositive(nums, expected):
    sol = Solution()
    assert sol.firstMissingPositive(nums) == expected
