import pytest
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh, t = 0, 0
        q = deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j])

        def isValid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
                    X, Y = x + dx, y + dy
                    if isValid(X, Y):
                        grid[X][Y] = 2
                        q.append([X, Y])
                        fresh -= 1
            t += 1

        return t if fresh == 0 else -1


@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize(
    "grid, expected",
    [
        # Basic case
        ([[2,1,1],[1,1,0],[0,1,1]], 4),

        # All already rotten
        ([[2,2],[2,2]], 0),

        # Impossible case (some fresh never reachable)
        ([[2,1,1],[0,1,1],[1,0,1]], -1),

        # Only one fresh surrounded by 0s
        ([[0,0,0],[0,1,0],[0,0,0]], -1),

        # No oranges at all
        ([[0,0,0],[0,0,0]], 0),

        # No fresh oranges
        ([[2,0,0],[0,2,0]], 0),

        # No rotten oranges
        ([[1,1,1],[1,1,1]], -1),

        # Single fresh + single rotten adjacent
        ([[2,1]], 1),

        # Rotten in the corner, fresh spreads
        ([[2,1,1],[0,1,1],[1,0,1]], -1),

        # Fresh oranges in isolated clusters
        ([[2,1,1,0,1,1,2]], 2),

        # All fresh in a line, one rotten at one end
        ([[2,1,1,1,1,1]], 5),
    ]
)
def test_oranges_rotting(sol, grid, expected):
    # Deepcopy to prevent in-place mutation affecting other tests
    import copy
    assert sol.orangesRotting(copy.deepcopy(grid)) == expected
