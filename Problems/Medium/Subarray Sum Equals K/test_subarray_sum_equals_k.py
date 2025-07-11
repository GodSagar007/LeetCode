import pytest
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, seen = 0, defaultdict(int)
        seen[0] = 1

        prefixsum = 0
        for num in nums:
            prefixsum += num
            if prefixsum - k in seen:
                ans += seen[prefixsum - k]
            seen[prefixsum] += 1
        return ans

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize("nums, k, expected", [
    ([1, 1, 1], 2, 2),                    # two subarrays: [1,1] at start and middle
    ([1, 2, 3], 3, 2),                    # [3], [1,2]
    ([1], 1, 1),                          # single element equals k
    ([1, -1, 0], 0, 3),                   # [1,-1], [-1,0], [1,-1,0]
    ([0, 0, 0], 0, 6),                    # All subarrays sum to 0: 3*(3+1)/2 = 6
    ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),    # multiple scattered subarrays
    ([], 0, 0),                           # empty input
    ([1, 2, 1, 2, 1], 3, 4),              # overlapping valid subarrays
    ([-1, -1, 1], 0, 1),                  # [-1,-1,1] = 0
    ([1, 2, 3, -3, -2, 1], 3, 4),         # multiple valid subarrays including negatives
])
def test_subarray_sum_cases(sol, nums, k, expected):
    assert sol.subarraySum(nums, k) == expected
