from typing import List
import pytest

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]

@pytest.mark.parametrize(
    "s, wordDict, expected",
    [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("", ["a"], True),  # empty string can be segmented trivially
        ("a", ["a"], True),
        ("aaaaaaa", ["aaaa", "aaa"], True),
        ("aaaaaaa", ["aa", "aaa"], True),
        ("abcd", ["a", "abc", "b", "cd"], True),
        ("abcd", ["ab", "cd"], True),
        ("cars", ["car", "ca", "rs"], True),
        ("cars", ["car", "rs"], False),
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"], True),
    ]
)
def test_word_break(s, wordDict, expected):
    assert Solution().wordBreak(s, wordDict) == expected
