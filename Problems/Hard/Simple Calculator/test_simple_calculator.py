import pytest

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == '+':
                result += sign * number
                number = 0
                sign = 1

            elif ch == '-':
                result += sign * number
                number = 0
                sign = -1

            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif ch == ')':
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()

        result += sign * number
        return result


@pytest.mark.parametrize("expr, expected", [
    ("1 + 1", 2),                        # Basic addition
    ("2 - 1 + 2", 3),                    # Mix of operations
    ("(1+(4+5+2)-3)+(6+8)", 23),         # Nested parentheses
    ("-2 + 1", -1),                      # Negative start
    ("30 + (2 - 3)", 29),               # Multi-digit numbers
    ("(7)-(0)+(4)", 11),                # Parentheses with zero
    ("2147483647", 2147483647),         # Large number
    ("(1)", 1),                          # Single parentheses
    ("(1-(3-4))", 2),                    # Nested subtraction
    ("1 - (2 + (3 - (4 + 5)))", 5),      # Deep nesting
    ("", 0),                             # Empty input
    ("   ", 0),                          # Whitespace only
])
def test_calculate(expr, expected):
    sol = Solution()
    assert sol.calculate(expr) == expected
