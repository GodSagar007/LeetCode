import pytest
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque([])

        for i in range(len(nums)):
            while q and q[0] < i - k + 1:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                result.append(nums[q[0]])
        return result

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize("nums, k, expected", [
    ([1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]),   # classic example
    ([1], 1, [1]),                             # single element
    ([1, -1], 1, [1, -1]),                     # window of size 1
    ([9, 11], 2, [11]),                        # increasing order
    ([4, 3, 2, 1], 2, [4, 3, 2]),              # decreasing order
    ([1,3,1,2,0,5], 3, [3,3,2,5]),             # mix of highs and lows
    ([7, 2, 4], 2, [7, 4]),                    # peak at beginning and end
    ([1, 1, 1, 1], 2, [1, 1, 1]),              # all same values
    ([1, 3, 1, 3, 1, 3], 2, [3, 3, 3, 3, 3]),  # alternating highs
    ([1]*10000, 100, [1]*9901),               # large uniform array
])
def test_max_sliding_window(sol, nums, k, expected):
    assert sol.maxSlidingWindow(nums, k) == expected
