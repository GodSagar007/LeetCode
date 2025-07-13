import pytest
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in reversed(range(len(nums))):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], True),          # standard reachable case
    ([3, 2, 1, 0, 4], False),         # stuck at 0, can't reach end
    ([0], True),                     # already at the end
    ([1, 0], True),                  # one step forward is enough
    ([0, 1], False),                 # stuck at start
    ([2, 0, 0], True),               # jump over 0s
    ([1, 1, 0, 1], False),           # can't get past the zero
    ([5, 4, 3, 2, 1, 0, 0], False),  # can't reach end despite large start
    ([1]*10000, True),              # large reachable case
    ([9,8,7,6,5,4,3,2,1,0,0], False),# long but ends before reaching
])
def test_can_jump_cases(sol, nums, expected):
    assert sol.canJump(nums) == expected
