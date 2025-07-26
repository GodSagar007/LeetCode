from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        empty = []

        # Initialize row, column, and box sets
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3, j // 3)].add(val)
                else:
                    empty.append((i, j))

        def backtrack(index: int) -> bool:
            if index == len(empty):
                return True  # Puzzle solved

            i, j = empty[index]
            box_key = (i // 3, j // 3)

            for num in map(str, range(1, 10)):
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_key]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_key].add(num)

                    if backtrack(index + 1):
                        return True

                    # Backtrack
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_key].remove(num)

            return False

        backtrack(0)
