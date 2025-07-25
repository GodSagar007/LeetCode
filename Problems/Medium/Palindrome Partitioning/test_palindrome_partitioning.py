from typing import List
import pytest

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        backtrack(0, [])
        return res

@pytest.mark.parametrize("s, expected", [
    ("aab", [["a", "a", "b"], ["aa", "b"]]),
    ("a", [["a"]]),
    ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
    ("ab", [["a", "b"]]),
    ("racecar", [
        ["r", "a", "c", "e", "c", "a", "r"],
        ["r", "a", "c", "ece", "a", "r"],
        ["r", "a", "cec", "a", "r"],
        ["r", "aceca", "r"],
        ["racecar"]
    ]),
    ("", [[]])
])
def test_partition(s, expected):
    result = Solution().partition(s)
    # Sort each partition and the outer list for comparison (order doesn't matter)
    result_sorted = sorted([sorted(part) for part in result])
    expected_sorted = sorted([sorted(part) for part in expected])
    assert result_sorted == expected_sorted
