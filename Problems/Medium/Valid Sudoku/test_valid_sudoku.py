from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, box = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == ".":
                    continue
                if char in row[r] or char in col[c] or char in box[(r // 3, c // 3)]:
                    return False
                row[r].add(char)
                col[c].add(char)
                box[(r // 3, c // 3)].add(char)
        return True

# ✅ Pytest-compatible test function
def test_is_valid_sudoku():
    s = Solution()

    # ✅ Valid board
    board_valid = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert s.isValidSudoku(board_valid) == True

    # ❌ Invalid: duplicate in row
    board_row_dup = [
        ["5","3",".",".","7",".",".",".","5"],  # ← duplicate '5'
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert s.isValidSudoku(board_row_dup) == False

    # ❌ Invalid: duplicate in column
    board_col_dup = [
        ["5","3",".",".","7",".",".",".","."],
        ["6","6",".","1","9","5",".",".","."],  # ← duplicate '6'
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert s.isValidSudoku(board_col_dup) == False

    # ❌ Invalid: duplicate in 3x3 box
    board_box_dup = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".","3","1","9","5",".",".","."],  # ← duplicate '3' in top-left box
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert s.isValidSudoku(board_box_dup) == False

    # ✅ Edge Case: Empty board (all dots)
    empty_board = [["."] * 9 for _ in range(9)]
    assert s.isValidSudoku(empty_board) == True

# ✅ Optional: Run tests manually
if __name__ == "__main__":
    test_is_valid_sudoku()
    print("✅ All test cases passed.")
