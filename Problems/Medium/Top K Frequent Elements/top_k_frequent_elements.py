
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num,freq in count.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result

nums = [4, 4, 4, 4, 5, 5, 5, 6, 6, 7]
k = 3

sol = Solution()
result = sol.topKFrequent(nums,k)
print(result)
