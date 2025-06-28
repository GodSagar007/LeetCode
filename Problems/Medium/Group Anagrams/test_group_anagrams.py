import pytest
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(word)

        return [words for words in anagrams.values()]

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize(
    "strs, expected_groups",
    [
        # ✅ Basic case
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),

        # ✅ All anagrams
        (["abc", "bca", "cab", "cba", "bac", "acb"], [["abc", "bca", "cab", "cba", "bac", "acb"]]),

        # ✅ No anagrams
        (["a", "b", "c"], [["a"], ["b"], ["c"]]),

        # ✅ Mixed single and multiple anagrams
        ([""], [[""]]),
        (["", ""], [["", ""]]),
        (["a", ""], [["a"], [""]]),

        # ✅ Empty list
        ([], []),

        # ✅ Repeating letters
        (["aa", "aa", "aa"], [["aa", "aa", "aa"]]),

        # ✅ Anagrams with different word lengths (none are actually anagrams)
        (["abc", "de", "fgh"], [["abc"], ["de"], ["fgh"]]),

        # ✅ Anagrams with different ordering
        (["listen", "silent", "enlist", "inlets"], [["listen", "silent", "enlist", "inlets"]]),
    ]
)
def test_group_anagrams(sol, strs, expected_groups):
    result = sol.groupAnagrams(strs)

    # Convert both actual and expected groups to sets of frozensets for order-independent comparison
    result_set = {frozenset(group) for group in result}
    expected_set = {frozenset(group) for group in expected_groups}

    assert result_set == expected_set
