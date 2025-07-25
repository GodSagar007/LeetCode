import pytest
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]: 
        if not digits:
            return []       
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        def backtrack(idx, curr):
            if len(curr) == len(digits):
                result.append(curr[:])
                return
            digit = digits[idx]
            for char in digit_to_letters[digit]:
                backtrack(idx + 1, curr + char)
        
        backtrack(0, "")
        return result

@pytest.mark.parametrize(
    "digits,expected_output",
    [
        ("", []),  # No digits
        ("2", ["a", "b", "c"]),  # Single digit
        ("23", sorted([
            "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"
        ])),  # Two digits
        ("7", ["p", "q", "r", "s"]),  # Digit with 4 letters
        ("79", sorted([
            a + b for a in "pqrs" for b in "wxyz"
        ])),  # 4x4 = 16 combinations
    ]
)
def test_letterCombinations(digits, expected_output):
    assert sorted(Solution().letterCombinations(digits)) == sorted(expected_output)
