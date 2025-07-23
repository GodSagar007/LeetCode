class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key = lambda x: x[1])
        eend = -inf
        for start,end in intervals:
            if start<eend:
                ans+=1
            else:
                eend = end
        return ans
        

        
