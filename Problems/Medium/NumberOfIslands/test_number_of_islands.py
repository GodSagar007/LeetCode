import pytest

# Your original solution (placed above the tests)
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(x, y):
            if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        numIslands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    numIslands += 1
                    dfs(x, y)

        return numIslands

# --------------------------
# ✅ TEST CASES START HERE
# --------------------------

@pytest.mark.parametrize("grid, expected", [
    # ✅ Empty grid
    ([], 0),

    # ✅ Grid with only water
    ([["0", "0"], ["0", "0"]], 0),

    # ✅ Grid with only land (one big island)
    ([["1", "1"], ["1", "1"]], 1),

    # ✅ Grid with checkerboard pattern (every '1' is isolated)
    ([["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]], 5),

    # ✅ Multiple small islands
    ([["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]], 3),

    # ✅ Long horizontal island
    ([["1", "1", "1", "1", "1"]], 1),

    # ✅ Long vertical island
    ([["1"], ["1"], ["1"], ["1"]], 1),

    # ✅ Irregular island shapes
    ([["1", "0", "1", "0", "1"],
      ["0", "1", "0", "1", "0"],
      ["1", "0", "1", "0", "1"]], 8),
])
def test_num_islands(grid, expected):
    # Make a deep copy because the function mutates the input
    from copy import deepcopy
    s = Solution()
    assert s.numIslands(deepcopy(grid)) == expected
