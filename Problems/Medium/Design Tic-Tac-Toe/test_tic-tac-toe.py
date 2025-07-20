import pytest

# ---- TicTacToe class (included in the same file for testing) ----
class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        mark = 1 if player == 1 else -1
        self.rows[row] += mark
        self.cols[col] += mark
        if row == col:
            self.diag += mark
        if row + col == self.n - 1:
            self.anti_diag += mark

        if (
            abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diag) == self.n or
            abs(self.anti_diag) == self.n
        ):
            return player
        return 0

# ---- Parameterized pytest test cases ----
@pytest.mark.parametrize(
    "n, moves, expected_outputs",
    [
        # No winner, just some moves
        (3, [(0, 0, 1), (1, 1, 2)], [0, 0]),

        # Player 1 wins by first row
        (3, [(0, 0, 1), (1, 0, 2), (0, 1, 1), (1, 1, 2), (0, 2, 1)], [0, 0, 0, 0, 1]),

        # Player 2 wins by second column
        (3, [(0, 0, 1), (0, 1, 2), (1, 0, 1), (1, 1, 2), (2, 2, 1), (2, 1, 2)], [0, 0, 0, 0, 0, 2]),

        # Player 1 wins on main diagonal
        (3, [(0, 0, 1), (0, 1, 2), (1, 1, 1), (0, 2, 2), (2, 2, 1)], [0, 0, 0, 0, 1]),

        # Player 2 wins on anti-diagonal
        (3, [(0, 2, 2), (0, 0, 1), (1, 1, 2), (1, 0, 1), (2, 0, 2)], [0, 0, 0, 0, 2]),

        # Player 1 wins in column 2
        (3, [(0, 2, 1), (0, 0, 2), (1, 2, 1), (1, 0, 2), (2, 2, 1)], [0, 0, 0, 0, 1]),

        # Edge case: 1x1 board, instant win
        (1, [(0, 0, 1)], [1]),

        # No winner until last move, full game
        (3, [(0,0,1),(0,1,2),(0,2,1),(1,1,2),(1,0,1),(1,2,2),(2,1,1),(2,0,2),(2,2,1)], [0]*9),
    ]
)
def test_tictactoe(n, moves, expected_outputs):
    game = TicTacToe(n)
    results = [game.move(row, col, player) for (row, col, player) in moves]
    assert results == expected_outputs
