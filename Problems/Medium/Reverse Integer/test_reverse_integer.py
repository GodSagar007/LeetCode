import pytest

# Your solution class
class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        sign = [1, -1][x < 0]
        x = abs(x)
        ans = 0

        while x:
            x, rem = divmod(x, 10)
            ans = ans * 10 + rem
            if ans > MAX:
                return 0
        return sign * ans

# Test cases
@pytest.mark.parametrize("input_x, expected", [
    (123, 321),                # Basic positive
    (-123, -321),              # Basic negative
    (120, 21),                 # Ends with zero
    (0, 0),                    # Zero
    (1534236469, 0),           # Overflow on reverse
    (-1534236469, 0),          # Negative overflow
    (7463847412, 2147483647),  # Edge case just below overflow
    (2**31 - 1, 0),            # Max 32-bit signed int, overflows when reversed
    (-2**31, 0),               # Min 32-bit signed int, overflows when reversed
])
def test_reverse(input_x, expected):
    sol = Solution()
    assert sol.reverse(input_x) == expected
