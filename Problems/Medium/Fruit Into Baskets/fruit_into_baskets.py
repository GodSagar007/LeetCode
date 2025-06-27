from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1

            # Shrink window if we have more than 2 fruit types
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            # Update max window size
            max_len = max(max_len, right - left + 1)

        return max_len
