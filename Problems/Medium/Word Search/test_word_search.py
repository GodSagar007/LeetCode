import pytest
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, idx, seen):
            if idx == len(word):
                return True

            if (
                r < 0 or r == rows or
                c < 0 or c == cols or
                board[r][c] != word[idx] or
                (r, c) in seen
            ):
                return False

            seen.add((r, c))
            res = (
                backtrack(r + 1, c, idx + 1, seen) or
                backtrack(r - 1, c, idx + 1, seen) or
                backtrack(r, c + 1, idx + 1, seen) or
                backtrack(r, c - 1, idx + 1, seen)
            )
            seen.remove((r, c))
            return res

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0, set()):
                        return True

        return False


@pytest.mark.parametrize(
    "board, word, expected",
    [
        # ✅ Basic cases
        ([["A", "B", "C", "E"],
          ["S", "F", "C", "S"],
          ["A", "D", "E", "E"]],
         "ABCCED", True),

        ([["A", "B", "C", "E"],
          ["S", "F", "C", "S"],
          ["A", "D", "E", "E"]],
         "SEE", True),

        ([["A", "B", "C", "E"],
          ["S", "F", "C", "S"],
          ["A", "D", "E", "E"]],
         "ABCB", False),  # Path reuse not allowed

        # ✅ Edge cases
        ([["a"]], "a", True),
        ([["a"]], "b", False),
        ([["a", "b"], ["c", "d"]], "abcd", False),  # Not in order

        # ✅ Multi-path ambiguity
        ([["a", "b", "c", "e"],
          ["s", "f", "c", "s"],
          ["a", "d", "e", "e"]],
         "abcced", True),

        # ✅ Larger board
        ([["a", "b", "c", "e"],
          ["s", "f", "e", "s"],
          ["a", "d", "e", "e"]],
         "abceesee", False),

        # ✅ Path reuse disallowed
        ([["a", "a", "a", "a"],
          ["a", "a", "a", "a"],
          ["a", "a", "a", "a"]],
         "aaaaaaaaaaaaa", False),  # Too long for board

        # ✅ Empty board
        ([], "abc", False),

        # ✅ Empty word
        ([["a", "b"], ["c", "d"]], "", True),  # Technically true — empty path always exists
    ]
)
def test_exist(board, word, expected):
    sol = Solution()
    assert sol.exist(board, word) == expected
