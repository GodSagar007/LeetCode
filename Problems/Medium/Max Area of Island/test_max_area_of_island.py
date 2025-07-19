from typing import List
import pytest
from copy import deepcopy

# -------------------- Solution Class --------------------
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0

        def dfs(x, y):
            if x < 0 or x == m or y < 0 or y == n or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y - 1) + dfs(x, y + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)

        return maxArea

# -------------------- Test Function --------------------
@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0]], 0),
        ([[1]], 1),
        ([[1, 0, 1], [0, 1, 0]], 1),
        ([[1, 1], [1, 1]], 4),
        ([[0, 1, 0, 0, 1],
          [1, 1, 0, 0, 1],
          [0, 0, 0, 1, 1],
          [1, 0, 1, 1, 1]], 7),
        ([[1, 1, 0, 1]], 2),
        ([[1], [1], [0], [1]], 2),
        ([[0] * 10 for _ in range(8)], 0),
        ([[1] * 7 for _ in range(3)], 21),
        ([[ (i + j) % 2 for j in range(50)] for i in range(50)], 1),
    ],
)
def test_max_area_of_island(grid, expected):
    assert Solution().maxAreaOfIsland(deepcopy(grid)) == expected
