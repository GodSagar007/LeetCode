import pytest

from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [float('inf')] * (n + 1)
        dp[n - 1] = 1  # Need at least 1 health at the princess cell
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                min_health = min(dp[j], dp[j + 1]) - dungeon[i][j]
                dp[j] = max(1, min_health)
                
        return dp[0]

@pytest.mark.parametrize(
    "dungeon, expected",
    [
        # Single cell, negative value (most dangerous case)
        ([[-5]], 6),
        
        # Single cell, positive value (easy case)
        ([[10]], 1),
        
        # Small grid with only damage
        ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7),
        
        # Grid with mix of healing and damage
        ([[0, -3], [-10, 0]], 4),
        
        # Grid with all healing
        ([[5, 10], [20, 1]], 1),
        
        # Grid with all damage
        ([[-2, -3], [-4, -5]], 12),
        
        # Path where damage early, healing later
        ([[-2, -3, 10], [-5, 100, 1], [-10, -30, -5]], 3),
        
        # Only one row
        ([[-2, -3, -4]], 10),
        
        # Only one column
        ([[-2], [-3], [-4]], 10),
        
        # Large healing at start, damage later
        ([[100, -200], [-300, 1]], 201),
    ]
)
def test_calculate_minimum_hp(dungeon, expected):
    assert Solution().calculateMinimumHP(dungeon) == expected
