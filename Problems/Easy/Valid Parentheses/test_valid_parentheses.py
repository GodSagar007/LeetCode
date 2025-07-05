import pytest

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"(":")","[":"]","{":"}"}
        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            else:
                if not stack or pair[stack.pop()] != bracket:
                    return False
        return not stack

@pytest.mark.parametrize("s, expected", [
    ("()", True),                    # simple valid pair
    ("()[]{}", True),               # multiple valid types
    ("(]", False),                  # mismatch
    ("([)]", False),                # interleaved invalid
    ("{[]}", True),                 # nested valid
    ("", True),                     # empty string is valid
    ("(((((((())))))))", True),    # deeply nested single type
    ("(((((((()))))))", False),    # missing closing
    ("]", False),                   # starts with closing
    ("[", False),                   # only opening
    ("({[)", False),                # incomplete and interleaved
    ("({[]})", True),              # properly nested
    ("{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}", True),  # big nest
])
def test_is_valid(s: str, expected: bool):
    sol = Solution()
    assert sol.isValid(s) == expected
