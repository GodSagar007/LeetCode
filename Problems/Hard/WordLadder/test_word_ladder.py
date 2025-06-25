import pytest
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        q = deque([(beginWord, 1)])
        
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordList:
                        q.append((nextWord, steps + 1))
                        wordList.remove(nextWord)
        
        return 0

sol = Solution()

@pytest.mark.parametrize("beginWord, endWord, wordList, expected", [
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),  # Standard example
    ("hit", "cog", ["hot","dot","dog","lot","log"], 0),        # End word missing
    ("a", "c", ["a", "b", "c"], 2),                             # Single-letter transformation
    ("hit", "xyz", ["hot","dot","dog","lot","log","cog"], 0),  # No possible path
    ("hit", "hit", ["hit"], 1),                                # Start = end
    ("hit", "hit", ["hot"], 0),                                # Start = end but not in list
    ("", "", [], 0),                                           # Empty input
    ("hit", "cog", [], 0),                                     # Empty wordList
    ("hit", "cog", ["hot","dot","dog","lot","log","cog","hog"], 4),  # Alternative shorter path
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"] + [f"word{i}" for i in range(1000)], 5),  # Large wordList
])
def test_ladder_length(beginWord, endWord, wordList, expected):
    assert sol.ladderLength(beginWord, endWord, wordList) == expected
