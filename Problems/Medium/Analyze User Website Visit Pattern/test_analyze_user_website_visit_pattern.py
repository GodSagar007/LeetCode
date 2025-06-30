import pytest
from collections import defaultdict, Counter
from typing import List

# Your Solution class
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = sorted(zip(timestamp, username, website))

        userVisitPattern = defaultdict(list)
        for _, user, site in data:
            userVisitPattern[user].append(site)
        
        patternCount = Counter()
        for user, sites in userVisitPattern.items():
            n = len(sites)
            seen = set()

            for i in range(n - 2):
                for j in range(i + 1, n - 1):
                    for k in range(j + 1, n):
                        pattern = (sites[i], sites[j], sites[k])
                        if pattern not in seen:
                            seen.add(pattern)
                            patternCount[pattern] += 1
        if not patternCount:
            return []
        maxVisitedPattern = max(sorted(patternCount), key=lambda p: patternCount[p])
        return list(maxVisitedPattern)

# Test cases
@pytest.mark.parametrize("username, timestamp, website, expected", [
    (
        ["u1", "u1", "u1", "u2", "u2", "u2"],
        [1, 2, 3, 4, 5, 6],
        ["a", "b", "c", "a", "b", "a"],
        ["a", "b", "a"]
    ),
    (
        ["u1", "u2", "u1", "u2", "u1", "u2"],
        [1, 2, 3, 4, 5, 6],
        ["a", "a", "b", "b", "c", "c"],
        ["a", "b", "c"]
    ),
    (
        ["u1", "u1", "u1"],
        [1, 2, 3],
        ["z", "z", "z"],
        ["z", "z", "z"]
    ),
    (
        ["u1", "u2", "u3", "u4"],
        [1, 2, 3, 4],
        ["a", "a", "a", "a"],
        []
    ),
    (
        ["u1", "u2", "u1", "u2", "u1", "u2"],
        [1, 2, 3, 4, 5, 6],
        ["x", "x", "y", "y", "z", "z"],
        ["x", "y", "z"]
    ),
])
def test_most_visited_pattern(username, timestamp, website, expected):
    sol = Solution()
    assert sol.mostVisitedPattern(username, timestamp, website) == expected
