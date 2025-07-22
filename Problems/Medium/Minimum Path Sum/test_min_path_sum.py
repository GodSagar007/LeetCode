import pytest
from typing import List

# ----------------- Code Under Test -----------------
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i != m - 1 and j == n - 1:
                    grid[i][j] += grid[i + 1][j]
                elif j != n - 1 and i == m - 1:
                    grid[i][j] += grid[i][j + 1]
                elif i != m - 1 and j != n - 1:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])

        return grid[0][0]
# ---------------------------------------------------

# ---------------------- Tests ----------------------
@pytest.mark.parametrize("grid, expected", [
    # 1. Simple 2x2 grid
    ([[1, 2], [1, 1]], 3),  # path: 1 → 1 → 1

    # 2. Larger grid with multiple options
    ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),  # path: 1→3→1→1→1

    # 3. All 1s
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 5),  # path: all 1s (shortest path has 5 steps)

    # 4. Grid with larger numbers
    ([[5, 9, 6], [11, 5, 2]], 17),  # path: 5 → 9 → 5 → 2

    # 5. Single row
    ([[1, 2, 3, 4]], 10),

    # 6. Single column
    ([[1], [2], [3], [4]], 10),

    # 7. Just one element
    ([[7]], 7),
])
def test_min_path_sum(grid, expected):
    assert Solution().minPathSum(grid) == expected
