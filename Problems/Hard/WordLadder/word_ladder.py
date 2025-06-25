from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        q = deque([(beginWord,1)])

        while q:
            word,steps = q.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nextWord = word[:i]+c+word[i+1:]
                    if nextWord in wordList:
                        q.append((nextWord,steps+1))
                        wordList.remove(nextWord)
        
        return 0
