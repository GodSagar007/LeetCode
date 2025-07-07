import pytest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - 1

        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]


@pytest.mark.parametrize("s, expected", [
    ("babad", ["bab", "aba"]),  # Both are valid
    ("cbbd", ["bb"]),
    ("a", ["a"]),
    ("ac", ["a", "c"]),
    ("racecar", ["racecar"]),
    ("", [""]),
    ("aaa", ["aaa"]),
    ("abacdfgdcaba", ["aba", "cdc"]),
    ("abcde", ["a", "b", "c", "d", "e"]),
    ("forgeeksskeegfor", ["geeksskeeg"]),
])
def test_longest_palindrome(s, expected):
    sol = Solution()
    result = sol.longestPalindrome(s)
    assert result in expected
