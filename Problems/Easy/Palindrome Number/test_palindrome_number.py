import pytest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = str(x)
        return True if l == l[::-1] else False

@pytest.mark.parametrize("x, expected", [
    # ✅ Positive Palindromes
    (121, True),
    (0, True),
    (1221, True),
    (12321, True),
    (1, True),

    # ❌ Not Palindromes
    (123, False),
    (10, False),
    (1001, True),   # Still palindrome
    (123456, False),

    # ⚠️ Negative Numbers (not palindromes by definition)
    (-121, False),
    (-1, False),

    # ⚠️ Edge Cases
    (1000021, False),
    (1000000001, True),
])
def test_is_palindrome(x, expected):
    sol = Solution()
    assert sol.isPalindrome(x) == expected
