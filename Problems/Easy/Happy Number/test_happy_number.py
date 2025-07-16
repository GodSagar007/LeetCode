import pytest

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            summ = 0
            while n > 0:
                n, digit = divmod(n, 10)
                summ += digit ** 2
            return summ

        slow = n
        fast = n

        while fast != 1:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            if slow == fast:
                break

        return fast == 1


@pytest.mark.parametrize("input_n, expected", [
    (1, True),          # Edge case: 1 is always happy
    (7, True),          # 7 → 49 → 97 → 130 → 10 → 1
    (19, True),         # Common happy number
    (2, False),         # Smallest unhappy number
    (4, False),         # Gets stuck in loop: 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4
    (100, True),        # 100 → 1² + 0 + 0 = 1
    (1111111, True),   # Large number, happy
    (10, True),         # 1² + 0² = 1
    (111, False),       # Another unhappy
])
def test_isHappy(input_n, expected):
    sol = Solution()
    assert sol.isHappy(input_n) == expected
