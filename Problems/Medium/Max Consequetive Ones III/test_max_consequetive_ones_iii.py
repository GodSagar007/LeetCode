import pytest
from typing import List

# ----------  Solution under test  ----------
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:                 # window invalid → shrink from left
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1
# ------------------------------------------


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # 1️⃣  Basic examples
        ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),  # LeetCode sample
        ([0,0,1,1,1,0,0], 0, 3),          # k=0, take existing ones only
        ([0,0,1,1,1,0,0], 1, 4),          # flip one zero
        ([0,0,1,1,1,0,0], 2, 5),          # flip two zeros

        # 2️⃣  All ones / all zeros
        ([1,1,1,1], 0, 4),                # already all ones
        ([0,0,0,0], 2, 2),                # can flip at most 2 zeros
        ([0,0,0,0], 5, 4),                # flip all zeros (k>=zeros)

        # 3️⃣  Single‑element arrays
        ([1], 0, 1),
        ([0], 0, 0),
        ([0], 1, 1),

        # 4️⃣  k equals array length
        ([0,1,0,1], 4, 4),

        # 5️⃣  Alternating pattern
        ([1,0,1,0,1,0,1,0], 2, 5),

        # 6️⃣  Large block of zeros in middle
        ([1,1,1] + [0]*10 + [1,1], 3, 6),

        # 7️⃣  No zeros
        ([1,1,1,1,1], 3, 5),

        # 8️⃣  k == 0 but zeros split ones
        ([1,1,0,1,1,1,0,1], 0, 3),
    ],
)
def test_longest_ones(nums, k, expected):
    sol = Solution()
    assert sol.longestOnes(nums, k) == expected
