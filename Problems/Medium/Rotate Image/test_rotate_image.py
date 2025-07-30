from typing import List
import pytest

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(i + 1, c):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(r):
            for j in range(c // 2):
                matrix[i][j], matrix[i][c - j - 1] = matrix[i][c - j - 1], matrix[i][j]

@pytest.mark.parametrize("matrix, expected", [
    (
        [[1, 2], [3, 4]],
        [[3, 1], [4, 2]]
    ),
    (
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    ),
    (
        [[1]],
        [[1]]
    ),
    (
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
        [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
    ),
])
def test_rotate(matrix, expected):
    Solution().rotate(matrix)
    assert matrix == expected
