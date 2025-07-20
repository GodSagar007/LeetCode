import pytest
from typing import List

# --- Code under test ---------------------------------------------------------
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif summ < 0:
                    j += 1
                else:
                    k -= 1
        return result


# --- Helper for order‑independent comparison ---------------------------------
def normalize(triplets: List[List[int]]) -> List[tuple]:
    """
    Sort elements inside each triplet and sort the list of triplets
    so that ordering does not affect equality checks.
    """
    return sorted(tuple(sorted(t)) for t in triplets)


# --- Parameterized pytest cases ---------------------------------------------
@pytest.mark.parametrize(
    "nums, expected",
    [
        # 1. Empty input
        ([], []),
        # 2. Fewer than three elements
        ([0], []),
        ([0, 1], []),
        # 3. All zeros (many duplicates)
        ([0, 0, 0, 0], [[0, 0, 0]]),
        # 4. Typical example with positives, negatives, duplicates
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        # 5. No possible triplet
        ([1, 2, 3, 4, 5], []),
        # 6. Duplicates with a single valid triplet
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        # 7. Larger mixed set
        (
            [-4, -2, -1, 0, 1, 2, 3, 5],
            [
                [-4, -1, 5],
                [-4, 1, 3],
                [-2, -1, 3],
                [-2, 0, 2],
                [-1, 0, 1],
            ],
        ),
    ],
)
def test_three_sum(nums, expected):
    sol = Solution()
    result = sol.threeSum(nums[:])  # pass a copy to avoid in‑place side‑effects
    assert normalize(result) == normalize(expected)


# Optional: allow `python this_file.py` to run tests directly
if __name__ == "__main__":
    import sys, pytest as _pytest

    sys.exit(_pytest.main([__file__]))
