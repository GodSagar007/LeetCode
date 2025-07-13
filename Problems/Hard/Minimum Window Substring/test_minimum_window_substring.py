import pytest
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            while missing == 0:
                if end == 0 or right - left < end - start:
                    start, end = left, right

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return s[start:end]

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize("s, t, expected", [
    ("ADOBECODEBANC", "ABC", "BANC"),          # classic example
    ("a", "a", "a"),                           # single letter match
    ("a", "aa", ""),                           # not enough characters
    ("aaflslflsldkalskaaa", "aaa", "aaa"),     # repeated letters
    ("abcdebdde", "bde", "deb"),              # minimal valid window
    ("abc", "d", ""),                          # no match at all
    ("", "a", ""),                             # empty source
    ("a", "", ""),                             # empty target
    ("abcabdebac", "cda", "cabd"),             # optimal window with overlap
    ("bba", "ab", "ba"),                       # ordering in t doesn’t matter
    ("aa", "aa", "aa"),                        # exact match, duplicates
])
def test_min_window(sol, s, t, expected):
    assert sol.minWindow(s, t) == expected
