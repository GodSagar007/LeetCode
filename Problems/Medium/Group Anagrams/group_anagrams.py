class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord('a')] += 1
            anagrams[tuple(count)].append(word)
        
        return [words for words in anagrams.values()]
