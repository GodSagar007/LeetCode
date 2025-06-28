import pytest
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        trapped_water = 0
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]

        while l < r:
            if lMax < rMax:
                trapped_water += max(0, lMax - height[l])
                l += 1
                lMax = max(lMax, height[l])
            else:
                trapped_water += max(0, rMax - height[r])
                r -= 1
                rMax = max(rMax, height[r])

        return trapped_water

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize(
    "height, expected",
    [
        # Basic cases
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),
        
        # Edge cases
        ([], 0),                     # Empty input
        ([1], 0),                    # Single bar
        ([1,2], 0),                  # Two bars
        ([2,0,2], 2),                # Simple trap
        ([3,0,0,2,0,4], 10),         # Multiple traps
        ([0,1,2,3,4,5], 0),          # Increasing height
        ([5,4,3,2,1,0], 0),          # Decreasing height
        ([5,5,1,7,1,1,5,2,7,6], 23),# Complex case
        ([9,6,8,8,5,6,3], 3),        # Mid dip
    ]
)
def test_trap(sol, height, expected):
    assert sol.trap(height) == expected
