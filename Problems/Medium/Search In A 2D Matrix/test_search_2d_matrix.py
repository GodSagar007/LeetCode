import pytest
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        start, end = 0, R * C - 1
        while start <= end:
            mid = (start + end) // 2
            r, c = mid // C, mid % C
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize("matrix, target, expected", [
    (
        [[1, 3, 5, 7],
         [10, 11, 16, 20],
         [23, 30, 34, 60]], 3, True),  # present in first row
    (
        [[1, 3, 5, 7],
         [10, 11, 16, 20],
         [23, 30, 34, 60]], 13, False),  # not present
    (
        [[1]], 1, True),  # single element match
    (
        [[1]], 2, False),  # single element no match
    (
        [[1, 2, 3, 4, 5]], 4, True),  # single row
    (
        [[1], [3], [5], [7]], 5, True),  # single column
    (
        [[1], [3], [5], [7]], 6, False),  # single column no match
    (
        [[1, 3, 5], [7, 9, 11], [13, 15, 17]], 17, True),  # last element
    (
        [[1, 3, 5], [7, 9, 11], [13, 15, 17]], 0, False),  # smaller than all
    (
        [[1, 3, 5], [7, 9, 11], [13, 15, 17]], 20, False),  # greater than all
])
def test_search_matrix(sol, matrix, target, expected):
    assert sol.searchMatrix(matrix, target) == expected
