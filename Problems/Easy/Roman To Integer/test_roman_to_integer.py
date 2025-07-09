import pytest

class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans = 0
        for i in range(len(s)):
            if i == len(s) - 1 or mp[s[i]] >= mp[s[i + 1]]:
                ans += mp[s[i]]
            else:
                ans -= mp[s[i]]
        return ans

@pytest.mark.parametrize("s, expected", [
    # Simple numerals
    ("I", 1),
    ("V", 5),
    ("X", 10),
    ("L", 50),
    ("C", 100),
    ("D", 500),
    ("M", 1000),

    # Compound values
    ("III", 3),
    ("VIII", 8),
    ("LVIII", 58),         # L = 50, V = 5, III = 3
    ("MCMXCIV", 1994),     # M = 1000, CM = 900, XC = 90, IV = 4

    # Subtractive cases
    ("IV", 4),
    ("IX", 9),
    ("XL", 40),
    ("XC", 90),
    ("CD", 400),
    ("CM", 900),

    # Complex combinations
    ("MMMCMXCIX", 3999),   # Max value allowed in modern Roman numerals
    ("CCCLXIX", 369),
])
def test_roman_to_int(s, expected):
    sol = Solution()
    assert sol.romanToInt(s) == expected
