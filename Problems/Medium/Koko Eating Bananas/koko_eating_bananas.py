class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1,max(piles)
        ans = high

        while low<=high:
            k = low + (high-low)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours<=h:
                ans = min(ans,k)
                high = k-1
            else:
                low = k+1
        
        return ans

        
