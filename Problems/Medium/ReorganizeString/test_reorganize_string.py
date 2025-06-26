import pytest
from collections import Counter

# Place your reorganizeString solution here
class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""
        c = Counter(s)
        max_freq_char, max_freq = c.most_common(1)[0]
        if 2 * max_freq > len(s) + 1:
            return ""

        res = [""] * len(s)
        index = 0

        while max_freq:
            res[index] = max_freq_char
            index += 2
            max_freq -= 1
        del c[max_freq_char]

        for char in c.elements():
            if index >= len(s):
                index = 1
            res[index] = char
            index += 2

        return "".join(res)

# ----------------------
# ✅ TEST CASES
# ----------------------

@pytest.mark.parametrize("input_str, expected_valid, expected_impossible", [
    ("aab", True, False),          # Should return e.g., "aba"
    ("aaab", False, True),         # Not possible
    ("vvvlo", True, False),        # Possible: e.g., "vlvov"
    ("", True, False),             # Empty string is valid
    ("a", True, False),            # Single character is trivially valid
    ("aa", False, True),           # Not possible
    ("aabb", True, False),         # Should return e.g., "abab"
    ("aaabbb", True, False),       # "ababab" is valid
    ("aaaabbbb", True, False),     # Balanced: "abababab"
    ("aaaaabbbbcc", True, False),  # 'a' occurs 5 times in 11 chars → not possible
])
def test_reorganize_string(input_str, expected_valid, expected_impossible):
    sol = Solution()
    output = sol.reorganizeString(input_str)

    if expected_impossible:
        assert output == "", f"Expected no valid output for {input_str}, but got '{output}'"
    else:
        assert len(output) == len(input_str), f"Length mismatch for input {input_str}"
        assert sorted(output) == sorted(input_str), f"Character mismatch for input {input_str}"

        # Check no adjacent characters are same
        for i in range(1, len(output)):
            assert output[i] != output[i-1], f"Adjacent duplicate at {i}: '{output[i-1]}{output[i]}'"
