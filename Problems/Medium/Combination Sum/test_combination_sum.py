import pytest
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(set(candidates)) 
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # Reuse current
                path.pop()

        backtrack(0, [], 0)
        return result

# Helper function to normalize results for unordered comparison
def normalize(results: List[List[int]]) -> List[List[int]]:
    return sorted(sorted(r) for r in results)

@pytest.mark.parametrize("candidates, target, expected", [
    # Basic case
    ([2, 3, 6, 7], 7, [[7], [2, 2, 3]]),

    # Single element used multiple times
    ([2], 4, [[2, 2]]),

    # No combination possible
    ([2], 3, []),

    # No candidates
    ([], 7, []),

    # Larger case with multiple combinations
    ([2, 3, 5], 8, [[2,2,2,2],[2,3,3],[3,5]]),

    # Target is 0
    ([1, 2, 3], 0, [[]]),
    ])

def test_combination_sum(candidates, target, expected):
    sol = Solution()
    result = sol.combinationSum(candidates, target)
    assert normalize(result) == normalize(expected)
