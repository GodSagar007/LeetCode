from typing import List
import pytest

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)
        return stack


# ──────────────── TESTS ────────────────

@pytest.mark.parametrize(
    "asteroids, expected",
    [
        ([5, 10, 15], [5, 10, 15]),        # No collisions
        ([-5, -10, -1], [-5, -10, -1]),

        ([5, -5], []),                    # Equal magnitude
        ([10, -5], [10]),                # Right wins
        ([5, -10], [-10]),               # Left wins

        ([8, 3, -5], [8]),               # 3 destroyed
        ([10, 2, -5], [10]),
        ([1, 2, 3, -5], [-5]),
        ([2, -2, -2], [-2]),

        ([-2, -1, 1, 2], [-2, -1, 1, 2]),  # No collision
        ([-2, 1, -1, 2, -2], [-2]),

        ([], []),                        # Empty input
        ([42], [42]),                    # Single positive
        ([-42], [-42]),                  # Single negative
    ],
)
def test_asteroid_collision(asteroids, expected):
    assert Solution().asteroidCollision(asteroids) == expected


def test_input_integrity():
    data = [5, -3, 4]
    Solution().asteroidCollision(data)
    assert data == [5, -3, 4]
