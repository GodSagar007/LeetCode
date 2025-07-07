class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime,endTime,profit),key = lambda x: x[0])

        maxProfit = 0
        heap = []

        for s,e,p in jobs:
            while heap and heap[0][0] <= s:
                _,prof = heapq.heappop(heap)
                maxProfit = max(maxProfit,prof)
            
            heapq.heappush(heap,(e,maxProfit+p))
        
        while heap:
            _,prof = heapq.heappop(heap)
            maxProfit = max(maxProfit,prof)
        
        return maxProfit
        
