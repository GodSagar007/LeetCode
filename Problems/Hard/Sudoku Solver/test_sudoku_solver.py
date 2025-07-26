import pytest

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    empty.append((i, j))
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        def backtrack(k):
            if k == len(empty):
                return True
            i, j = empty[k]
            b = (i // 3) * 3 + (j // 3)
            for d in map(str, range(1, 10)):
                if d not in rows[i] and d not in cols[j] and d not in boxes[b]:
                    board[i][j] = d
                    rows[i].add(d)
                    cols[j].add(d)
                    boxes[b].add(d)
                    if backtrack(k + 1):
                        return True
                    board[i][j] = '.'
                    rows[i].remove(d)
                    cols[j].remove(d)
                    boxes[b].remove(d)
            return False

        backtrack(0)

# ----------------- Pytest Suite ------------------

@pytest.mark.parametrize("input_board, expected_board", [
    (
        [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        [
            ["5","3","4","6","7","8","9","1","2"],
            ["6","7","2","1","9","5","3","4","8"],
            ["1","9","8","3","4","2","5","6","7"],
            ["8","5","9","7","6","1","4","2","3"],
            ["4","2","6","8","5","3","7","9","1"],
            ["7","1","3","9","2","4","8","5","6"],
            ["9","6","1","5","3","7","2","8","4"],
            ["2","8","7","4","1","9","6","3","5"],
            ["3","4","5","2","8","6","1","7","9"]
        ]
    ),
    # Add more test cases here if needed
])
def test_solve_sudoku(input_board, expected_board):
    Solution().solveSudoku(input_board)
    assert input_board == expected_board
