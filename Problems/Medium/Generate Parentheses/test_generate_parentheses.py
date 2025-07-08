from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(oc, cc, path):
            if len(path) == 2 * n:
                output.append(path[:])
                return
            if oc < n:
                backtrack(oc + 1, cc, path + '(')
            if cc < oc:
                backtrack(oc, cc + 1, path + ')')
        backtrack(0, 0, "")
        return output

# ✅ Tests
def test_generateParenthesis():
    s = Solution()

    # Edge: n = 0
    assert s.generateParenthesis(0) == [""]

    # Basic: n = 1
    assert sorted(s.generateParenthesis(1)) == ["()"]

    # Small: n = 2
    assert sorted(s.generateParenthesis(2)) == ["(())", "()()"]

    # Core test: n = 3
    assert sorted(s.generateParenthesis(3)) == sorted([
        "((()))", "(()())", "(())()", "()(())", "()()()"
    ])

    # Large: n = 4 (just check count)
    assert len(s.generateParenthesis(4)) == 14


    print("✅ All test cases passed")
