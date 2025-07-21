import pytest
from typing import List

# ------------- Code under test (assumed to be in the same file) -------------
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if mid % 2 == 1:          # make mid even
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                low = mid + 2         # single is to the right
            else:
                high = mid            # single is at mid or to the left
        return nums[low]
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "nums, expected",
    [
        # 1. Single element array
        ([7], 7),

        # 2. Single at the beginning
        ([0, 1, 1], 0),

        # 3. Single at the end (odd length)
        ([1, 1, 2], 2),

        # 4. Single in the middle
        ([1, 1, 2, 3, 3], 2),

        # 5. LeetCode sample 1
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),

        # 6. LeetCode sample 2
        ([3, 3, 7, 7, 10, 11, 11], 10),

        # 7. Larger array, single near the end
        ([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6], 4),

        # 8. Larger array, single at the very end
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6], 6),
    ],
)
def test_single_non_duplicate(nums, expected):
    assert Solution().singleNonDuplicate(nums) == expected
