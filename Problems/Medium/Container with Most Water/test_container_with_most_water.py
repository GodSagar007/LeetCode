import pytest
from typing import List

# -------------------- Code Under Test --------------------
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0
        while l < r:
            max_water = max(max_water, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water
# ---------------------------------------------------------


# ----------------------- Test Cases ----------------------
@pytest.mark.parametrize("height, expected", [
    ([1,8,6,2,5,4,8,3,7], 49),          # Wide & tall combo (classic example)
    ([1,1], 1),                         # Minimum valid input
    ([4,3,2,1,4], 16),                  # Tall sides enclosing max area
    ([1,2,1], 2),                       # Middle is tallest
    ([1,3,2,5,25,24,5], 24),           # Non-symmetric shape
    ([1,2,4,3], 4),                     # Slight asymmetry
    ([0,0,0,0,0,0,0], 0),              # All zero heights
    ([1000, 1, 1000], 2000),           # Narrow but tall at ends
    (list(range(1, 101)), 2500),       # Increasing: max is between 1 and 100
    (list(reversed(range(1, 101))), 2500),  # Decreasing: same as above
])
def test_max_area(height, expected):
    assert Solution().maxArea(height) == expected
# ----------------------------------------------------------
