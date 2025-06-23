import pytest
from typing import List
from termcolor import cprint

# === Self-contained Solution class ===
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [idx, seen[complement]]
            seen[num] = idx
        return [None, None]

sol = Solution()

# === Safe comparison function ===
def safe_compare(a, b):
    if a == [None, None] and b == [None, None]:
        return True
    if None in a or None in b:
        return False
    return sorted(a) == sorted(b)

# === Parametrized test with safe comparison ===
@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),              # basic case
    ([3, 3], 6, [0, 1]),                      # duplicate numbers
    ([-1, -2, -3, -4, -5], -8, [2, 4]),       # negative numbers
    ([1, 2, 3, -3], 0, [2, 3]),              # zero target
    ([], 10, [None, None]),                  # empty input
    ([5], 5, [None, None]),                  # single element
    ([1, 2, 3], 10, [None, None]),           # no valid pair
])
def test_two_sum(nums, target, expected):
    result = sol.twoSum(nums, target)
    passed = safe_compare(result, expected)

    if passed:
        cprint(f"✅ Passed: nums={nums}, target={target}, result={result}", "green")
    else:
        cprint(f"❌ Failed: nums={nums}, target={target}, result={result}, expected={expected}", "red")

    assert passed
