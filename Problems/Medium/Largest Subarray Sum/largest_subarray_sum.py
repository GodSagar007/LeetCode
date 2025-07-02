class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = float('-inf')
        curr = 0
        for num in nums:
            curr+=num
            largest = max(largest,curr)
            if curr<0:
                curr = 0
        
        return largest
            
