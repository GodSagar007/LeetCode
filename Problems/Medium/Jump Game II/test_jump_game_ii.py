import pytest
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumps, farthest, currEnd = 0, 0, 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == currEnd:
                minJumps += 1
                currEnd = farthest
        return minJumps

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], 2),              # basic case
    ([0], 0),                          # already at the end
    ([1, 0], 1),                       # 1 jump to reach
    ([1, 1, 1, 1], 3),                 # must jump every step
    ([5, 1, 1, 1, 1, 1], 1),           # one big jump from start
    ([3, 0, 0, 0], 1),                 # jump over zeros
    ([2, 3, 0, 1, 4], 2),              # last jump is exact
    ([4, 0, 0, 0, 4, 0, 0, 0, 1], 2),  # alternating big/zero jumps
    ([1] * 1000, 999),                 # large input, minimal jump distance
])
def test_jump_cases(sol, nums, expected):
    assert sol.jump(nums) == expected
