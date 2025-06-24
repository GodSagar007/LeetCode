import pytest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, longest = 0, 0

        for r in range(len(s)):
            if s[r] not in seen or seen[s[r]] < l:
                longest = max(longest, r - l + 1)
            else:
                l = seen[s[r]] + 1
            seen[s[r]] = r

        return longest

sol = Solution()

@pytest.mark.parametrize("input_str, expected", [
    ("abcabcbb", 3),           # Repeating after unique sequence
    ("bbbbb", 1),              # All characters same
    ("pwwkew", 3),             # Non-adjacent repeat
    ("", 0),                   # Empty string
    (" ", 1),                  # Single character (space)
    ("abcdef", 6),             # All unique characters
    ("abba", 2),               # Repeating in the middle
    ("tmmzuxt", 5),            # Random characters with repeats
    ("dvdf", 3),               # Multiple repeat points
    ("anviaj", 5),             # Complex pattern
    ("a" * 10000, 1),          # Long input with one repeating char
    ("".join(chr(i) for i in range(128)), 128),  # All ASCII characters
    ("a" * 9999 + "b", 2),     # Large size, one differing char at end
    ("abcadefg", 7),           # One repeat early
])
def test_length_of_longest_substring(input_str, expected):
    assert sol.lengthOfLongestSubstring(input_str) == expected
