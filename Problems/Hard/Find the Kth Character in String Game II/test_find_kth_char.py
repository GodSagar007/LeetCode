import math
from typing import List
import pytest

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        count = 0
        total_ops = len(operations)

        while k != 1:
            jump = math.ceil(math.log2(k))
            idx = jump - 1
            if idx >= total_ops:
                idx = total_ops - 1
            count += operations[idx]
            k -= 2 ** (jump - 1)

        count %= 26
        return chr(97 + count)

# -------------------- TESTS --------------------

@pytest.mark.parametrize(
    "k, operations, expected",
    [
        (1, [], "a"),                    # Base case: kth is the first character
        (2, [0], "a"),                   # "a" → "aa"
        (2, [1], "b"),                   # "a" → "ab"
        (3, [1, 1], "c"),                # "a" → "ab" → "abcd", 3rd char is 'c'
        (4, [1, 1], "d"),                # "a" → "ab" → "abcd", 4th char is 'd'
        (5, [1, 0], "b"),                # "a" → "ab" → "abab", 5th char is 'b'
        (6, [1, 1], "c"),                # "a" → "ab" → "abcd", 6th char is 'c'
        (8, [0, 0, 1], "b"),             # Final string doubles twice then adds transformed: "a" → "aa" → "aaaa" → "aaaabbbb"
        (10, [1, 0, 1], "c"),            # Apply transformations in middle
        (1024, [0]*10, "a"),             # Very long string via duplication, no transformation
        (1000, [1]*15, "p"),             # Many 1s, position 1000
    ]
)
def test_kthCharacter(k, operations, expected):
    assert Solution().kthCharacter(k, operations) == expected
