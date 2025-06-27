from collections import defaultdict
import pytest

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


# ✅ Pytest test cases
@pytest.mark.parametrize("fruits, expected", [
    ([1, 2, 1], 3),                         # basic
    ([1, 2, 3, 2, 2], 4),                   # third type in between
    ([1, 1, 1, 1], 4),                      # only one type
    ([0, 1, 2, 2], 3),                      # window ends early
    ([1, 2, 1, 2, 1, 2], 6),                # alternating two types
    ([1, 2, 3, 4, 5], 2),                   # all unique
    ([1, 1, 2, 2, 3, 3, 4, 4], 4),          # 2 repeating groups
    ([1]*100 + [2]*100 + [3]*100, 200),     # large input
    ([1,2,1,3,4,3,5,1,2,1,1,2,2,3,3], 5),   # mixed pattern
    ([], 0),                                # empty input
    ([1], 1),                               # single tree
    ([1, 2], 2),                            # only two types
    ([1, 2, 3], 2),                         # minimum cut at 3rd
])
def test_total_fruit(fruits, expected):
    output = Solution().totalFruit(fruits)
    assert output == expected, f"Expected {expected}, but got {output} from input {fruits}"
