import pytest
from typing import List

# ---------------- Code under test (same file) ----------------
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        no_del = arr[0]          # max sum with no deletion
        one_del = float("-inf")  # max sum with exactly one deletion
        max_sum = no_del

        for i in range(1, n):
            one_del = max(one_del + arr[i], no_del)   # delete current or deleted before
            no_del  = max(no_del + arr[i], arr[i])    # extend or restart
            max_sum = max(max_sum, no_del, one_del)

        return max_sum
# -------------------------------------------------------------


@pytest.mark.parametrize(
    "arr, expected",
    [
        # 1️⃣  Single positive element
        ([5], 5),

        # 2️⃣  Single negative element (nothing can be deleted)
        ([-3], -3),

        # 3️⃣  Mixed, best by deleting a negative in middle
        ([1, -2, 0, 3], 4),          # delete -2 → 1 + 0 + 3 = 4

        # 4️⃣  Larger mix, delete -10 in the middle segment
        ([1, -2, 3, 4, -10, 10], 17),  # choose [3,4,-10,10], delete -10 → 17

        # 5️⃣  All negatives, pick the least‑negative value
        ([-1, -2, -3], -1),

        # 6️⃣  All positives, no deletion needed
        ([2, 3, 4], 9),

        # 7️⃣  Two consecutive negatives, delete one of them
        ([10, -5, -5, 10], 15),      # delete either -5 inside full subarray

        # 8️⃣  Alternating 1 / -1
        ([1, -1, 1, -1, 1], 2),      # subarray [1,-1,1,-1,1] delete any -1 → 2

        # 9️⃣  Length‑2 array
        ([1, -2], 1),                # delete -2
    ],
)
def test_maximum_sum(arr, expected):
    assert Solution().maximumSum(arr) == expected
