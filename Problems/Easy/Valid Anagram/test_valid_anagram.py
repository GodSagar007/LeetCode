from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


import pytest

@pytest.mark.parametrize("s, t, expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("a", "a", True),
    ("", "", True),
    ("aacc", "ccac", False),
    ("night", "thing", True),
    ("abcd", "abcde", False),
])
def test_is_anagram(s, t, expected):
    sol = Solution()
    assert sol.isAnagram(s, t) == expected
