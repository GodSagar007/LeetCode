import pytest

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


@pytest.mark.parametrize("coins, amount, expected", [
    # Classic examples
    ([1, 2, 5], 11, 3),      # 5+5+1
    ([2], 3, -1),            # Cannot make 3 with only coin 2
    ([1], 0, 0),             # No coins needed to make 0
    ([1], 2, 2),             # Two 1s to make 2

    # Edge cases
    ([1, 3, 4], 6, 2),       # 3+3 or 4+1+1
    ([2, 5, 10, 1], 27, 4),  # 10+10+5+2
    ([186, 419, 83, 408], 6249, 20),  # Large input from LeetCode

    # Impossible cases
    ([2, 4], 7, -1),
    ([5, 10], 1, -1),

    # Minimal coin case
    ([7, 14], 49, 4),        # 14*3+7

    # Greedy trap
    ([1, 3, 4], 6, 2),       # Greedy would pick 4 + 1 + 1 (3 coins), optimal is 3 + 3 (2 coins)

    # Large amount, small coins
    ([1, 2, 5], 100, 20),    # 20 coins of 5

    # Amount = 1
    ([2, 5], 1, -1),
    ([1, 2], 1, 1)
])
def test_coin_change(coins, amount, expected):
    sol = Solution()
    assert sol.coinChange(coins, amount) == expected
