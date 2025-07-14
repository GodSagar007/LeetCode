import pytest
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        idx = -1
        for i in reversed(range(n - 1)):
            if nums[i] < nums[i + 1]:
                idx = i
                break
        if idx == -1:
            nums.sort()
            return
        for i in reversed(range(idx + 1, n)):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break
        nums[idx + 1:] = reversed(nums[idx + 1:])

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], [1, 3, 2]),         # basic increasing
    ([3, 2, 1], [1, 2, 3]),         # last permutation → reset
    ([1, 1, 5], [1, 5, 1]),         # with duplicates
    ([1], [1]),                     # single element
    ([1, 3, 2], [2, 1, 3]),         # non-trivial middle permutation
    ([2, 3, 1], [3, 1, 2]),         # end needs rolling back
    ([2, 1, 3], [2, 3, 1]),         # next lexicographic
    ([1, 5, 1], [5, 1, 1]),         # repeated numbers
    ([1, 4, 3, 2], [2, 1, 3, 4]),   # tail almost reversed
    ([1, 2, 4, 3], [1, 3, 2, 4]),   # deeper swap
])
def test_next_permutation(nums, expected):
    sol = Solution()
    sol.nextPermutation(nums)
    assert nums == expected
