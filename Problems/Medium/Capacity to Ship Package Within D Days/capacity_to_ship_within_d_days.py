class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high = max(weights),sum(weights)
        ans = high
        def calcDays(capacity):
            d = 1
            curr = 0
            for weight in weights:
                if curr + weight > capacity:
                    curr = 0
                    d+=1
                curr+=weight
            return d

        while low<=high:
            mid = (low+high)//2
            needed  = calcDays(mid)
            if needed <=days:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        
        return ans
            
        
