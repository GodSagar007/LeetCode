from typing import List
import pytest

# Solution code
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

# Test cases
@pytest.mark.parametrize("nums, expected", [
    ([2, 2, 1], 1),               # basic case
    ([4, 1, 2, 1, 2], 4),         # single outlier at front
    ([1], 1),                     # single element
    ([0, 0, 99], 99),             # zeroes with one unique
    ([17, 3, 3], 17),             # small custom case
    ([10**6, 1, 1], 10**6),       # large number with small duplicates
])
def test_single_number(nums, expected):
    sol = Solution()
    assert sol.singleNumber(nums) == expected
