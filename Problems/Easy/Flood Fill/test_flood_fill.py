import pytest
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0] or image[sr][sc] == color: 
            return image
        def dfs(x, y, org, new):
            if x < 0 or x == len(image) or y < 0 or y == len(image[0]) or image[x][y] != org:
                return
            image[x][y] = new
            dfs(x + 1, y, org, new)
            dfs(x, y + 1, org, new)
            dfs(x - 1, y, org, new)
            dfs(x, y - 1, org, new)

        dfs(sr, sc, image[sr][sc], color)
        return image

@pytest.mark.parametrize("image, sr, sc, color, expected", [
    # Test case 1: Normal fill
    ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2, [[2,2,2],[2,2,0],[2,0,1]]),

    # Test case 2: No change needed
    ([[0,0,0],[0,0,0]], 0, 0, 0, [[0,0,0],[0,0,0]]),

    # Test case 3: Single cell image
    ([[1]], 0, 0, 2, [[2]]),

    # Test case 4: Filling from an edge
    ([[0,0,0],[0,1,1]], 1, 1, 1, [[0,0,0],[0,1,1]]),

    # Test case 5: Multiple regions
    ([[0,0,0],[0,1,1]], 1, 1, 2, [[0,0,0],[0,2,2]]),

    # Test case 6: Full fill
    ([[1,1],[1,1]], 0, 0, 9, [[9,9],[9,9]]),

    # Test case 7: Diagonals not connected
    ([[1,2,3],[4,1,6],[7,8,1]], 0, 0, 5, [[5,2,3],[4,1,6],[7,8,1]]),

    # Test case 8: Empty image (should not crash)
    ([[]], 0, 0, 1, [[]]),

    # Test case 9: Large color same as existing in corner
    ([[3,3,3],[3,1,1],[3,3,3]], 1, 1, 1, [[3,3,3],[3,1,1],[3,3,3]])
])
def test_flood_fill(image, sr, sc, color, expected):
    sol = Solution()
    assert sol.floodFill(image, sr, sc, color) == expected
