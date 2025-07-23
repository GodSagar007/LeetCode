import pytest
from typing import List
from math import inf

# -------------------- Code Under Test --------------------
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key=lambda x: x[1])
        eend = -inf
        for start, end in intervals:
            if start < eend:
                ans += 1
            else:
                eend = end
        return ans
# ----------------------------------------------------------


# ------------------------ Tests ---------------------------
@pytest.mark.parametrize("intervals, expected", [
    ([[1,2],[2,3],[3,4],[1,3]], 1),          # Remove [1,3]
    ([[1,2],[1,2],[1,2]], 2),                # Remove any two
    ([[1,2],[2,3]], 0),                      # No overlap
    ([[1,5],[2,6],[3,7],[4,8]], 3),          # Fully overlapping
    ([[1,100],[11,22],[1,11],[2,12]], 2),    # Sort helps avoid multiple removals
    ([[0,2],[1,3],[2,4],[3,5],[4,6]], 2),     # Remove overlapping middles
    ([[1,2]], 0),                            # Single interval
    ([], 0),                                 # Empty input
])
def test_erase_overlap_intervals(intervals, expected):
    assert Solution().eraseOverlapIntervals(intervals) == expected
# ----------------------------------------------------------
