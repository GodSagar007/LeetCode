import pytest

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)
        while k > 0:
            stack.pop()
            k -= 1
        result = "".join(stack).lstrip('0') or '0'
        return result

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize(
    "num, k, expected",
    [
        # Basic case
        ("1432219", 3, "1219"),
        # Remove all digits
        ("10", 2, "0"),
        # Leading zeros in result
        ("10200", 1, "200"),
        # Removing only digit
        ("9", 1, "0"),
        # No digits removed
        ("123456", 0, "123456"),
        # Remove all digits to get 0
        ("123456", 6, "0"),
        # All same digits
        ("11111", 3, "11"),
        # k > 1 but partial removal
        ("112", 1, "11"),
        ("112", 2, "1"),
        # Already minimal
        ("123", 1, "12"),
        # Multiple leading zeros after removal
        ("100200", 1, "200"),
        ("100200", 2, "0"),
        # Descending number (maximal removal)
        ("7654321", 3, "4321"),
        # Edge: k = 0, no-op
        ("765", 0, "765"),
        # Large k with short number
        ("10", 1, "0"),
        # Number becomes zero
        ("100", 1, "0"),
    ]
)
def test_remove_kdigits(sol, num, k, expected):
    assert sol.removeKdigits(num, k) == expected
