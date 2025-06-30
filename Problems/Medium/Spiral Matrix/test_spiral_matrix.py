import pytest
from typing import List

# Your Solution class
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rs, cs = 0, 0
        re, ce = len(matrix) - 1, len(matrix[0]) - 1
        ans = []

        while rs <= re and cs <= ce:
            for c in range(cs, ce + 1):
                ans.append(matrix[rs][c])
            rs += 1

            for r in range(rs, re + 1):
                ans.append(matrix[r][ce])
            ce -= 1

            if rs <= re:
                for c in range(ce, cs - 1, -1):
                    ans.append(matrix[re][c])
                re -= 1

            if cs <= ce:
                for r in range(re, rs - 1, -1):
                    ans.append(matrix[r][cs])
                cs += 1

        return ans


# Test cases
@pytest.mark.parametrize("matrix, expected", [
    # Square matrix
    ([[1, 2], [4, 3]], [1, 2, 3, 4]),

    # Rectangular (more columns)
    ([[1, 2, 3], [6, 5, 4]], [1, 2, 3, 4, 5, 6]),

    # Rectangular (more rows)
    ([[1, 2], [6, 3], [5, 4]], [1, 2, 3, 4, 5, 6]),

    # Single row
    ([[1, 2, 3, 4]], [1, 2, 3, 4]),

    # Single column
    ([[1], [2], [3], [4]], [1, 2, 3, 4]),

    # 3x3 square matrix
    ([[1, 2, 3], [8, 9, 4], [7, 6, 5]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),

    # 4x4 square matrix
    ([[1, 2, 3, 4],
      [12,13,14,5],
      [11,16,15,6],
      [10, 9, 8,7]], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]),

    # Empty matrix
    ([], []),

    # Matrix with one element
    ([[42]], [42]),
])
def test_spiral_order(matrix, expected):
    sol = Solution()
    assert sol.spiralOrder(matrix) == expected
