import pytest

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        largest = float('-inf')
        curr = 0
        for num in nums:
            curr += num
            largest = max(largest, curr)
            if curr < 0:
                curr = 0
        return largest


@pytest.mark.parametrize("nums, expected", [
    ([1], 1),                            # Single positive element
    ([-1], -1),                          # Single negative element
    ([1, 2, 3, 4], 10),                  # All positive
    ([-2, -3, -1, -4], -1),              # All negative
    ([5, -2, 3, 4], 10),                 # Positive dips
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),# Mixed values (classic case)
    ([0, 0, 0, 0], 0),                   # All zeros
    ([2, -1, 2, 3, 4, -5], 10),          # Dips but big subarray
    ([8, -19, 5, -4, 20], 21),           # Big late subarray
    ([3, -2, 5, -1], 6),                 # Small variations
])
def test_max_subarray(nums, expected):
    sol = Solution()
    assert sol.maxSubArray(nums) == expected
