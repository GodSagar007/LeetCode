class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l,longest = 0,0

        for r in range(len(s)):
            if s[r] not in seen or seen[s[r]] < l:
                longest = max(longest,r-l+1)
            else:
                l = seen[s[r]] + 1
            seen[s[r]] = r
        
        return longest

        
