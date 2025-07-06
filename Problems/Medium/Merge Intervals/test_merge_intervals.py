from typing import List
import pytest

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        result = []
        for start, end in intervals:
            if not result or result[-1][1] < start:
                result.append([start, end])
            else:
                result[-1][1] = max(result[-1][1], end)
        return result


@pytest.mark.parametrize("intervals, expected", [
    # Empty input
    ([], []),

    # Single interval
    ([[1, 3]], [[1, 3]]),

    # No overlap
    ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),

    # Some overlapping intervals
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),

    # Overlapping chain
    ([[1, 4], [2, 5], [5, 7]], [[1, 7]]),

    # Fully nested intervals
    ([[1, 10], [2, 3], [4, 8]], [[1, 10]]),

    # Unordered input
    ([[5, 6], [1, 3], [2, 4]], [[1, 4], [5, 6]]),

    # Duplicate intervals
    ([[1, 3], [1, 3], [2, 6]], [[1, 6]]),

    # Already merged
    ([[1, 5], [6, 10]], [[1, 5], [6, 10]]),

    # Touching boundaries
    ([[1, 4], [4, 5]], [[1, 5]]),

    # Negative values
    ([[-10, -1], [-5, 0], [1, 3]], [[-10, 0], [1, 3]]),

    # All collapse into one
    ([[1, 4], [2, 3], [3, 5]], [[1, 5]])
])
def test_merge(intervals: List[List[int]], expected: List[List[int]]):
    s = Solution()
    assert s.merge(intervals) == expected
