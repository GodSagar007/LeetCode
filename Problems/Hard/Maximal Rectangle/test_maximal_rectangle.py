import pytest
from typing import List

# ------------- Code under test (assumed to be in the same file) -------------
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        height = [0] * cols
        best = 0

        for r in range(rows):
            # Build histogram heights for row r
            for c in range(cols):
                height[c] = height[c] + 1 if matrix[r][c] == '1' else 0

            # Largest Rectangle in Histogram (monotone stack)
            stack = []
            for i in range(cols + 1):                         # sentinel
                cur_h = height[i] if i < cols else 0
                while stack and cur_h < height[stack[-1]]:
                    h = height[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    best = max(best, h * width)
                stack.append(i)

        return best
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "matrix, expected",
    [
        # 1. Empty matrix
        ([], 0),

        # 2. Single cell (0 and 1)
        ([["0"]], 0),
        ([["1"]], 1),

        # 3. 2×2 fully filled
        ([["1", "1"],
          ["1", "1"]], 4),

        # 4. LeetCode example
        ([["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]], 6),

        # 5. Checkerboard 2×2 (no rectangle >1)
        ([["0", "1"],
          ["1", "0"]], 1),

        # 6. Single row
        ([["1", "1", "0", "1"]], 2),

        # 7. Single column
        ([["1"], ["1"], ["1"], ["0"], ["1"]], 3),

        # 8. Tall rectangle (3×5 with top two rows full of 1s)
        ([["1", "1", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["0", "0", "1", "1", "1"]], 10),

        # 9. Wide but shallow irregular
        ([["1", "0", "1", "1", "1", "1"]], 4),
    ],
)
def test_maximal_rectangle(matrix, expected):
    assert Solution().maximalRectangle(matrix) == expected
