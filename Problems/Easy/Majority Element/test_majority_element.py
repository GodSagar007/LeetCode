from typing import List
import pytest

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me, count = None, 0
        for num in nums:
            if num == me:
                count += 1
            else:
                if count == 0:
                    me = num
                    count = 1
                else:
                    count -= 1
        return me

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 3, 4], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([6, 5, 5], 5),
        ([8, 8, 7, 7, 7, 8, 8], 8),
        ([9, 9, 9, 1, 2, 3, 9], 9),
        ([4, 4, 4, 4, 4, 5, 5, 5], 4),  # 4 is more than n//2
    ]
)
def test_majority_element(nums, expected):
    assert Solution().majorityElement(nums) == expected
