class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


import pytest

@pytest.mark.parametrize("n, expected", [
    (1, 1),     # Only one step: [1]
    (2, 2),     # [1+1], [2]
    (3, 3),     # [1+1+1], [1+2], [2+1]
    (4, 5),     # 5 combinations total
    (5, 8),     # Fibonacci(5+1)
    (6, 13),
    (10, 89),
    (20, 10946),
])
def test_climb_stairs(n, expected):
    sol = Solution()
    assert sol.climbStairs(n) == expected
