class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        ans = 0
        window_sum  = 0

        for r in range(len(nums)):
            window_sum += nums[r]
            while nums[r] * (r-l+1) - window_sum > k:
                window_sum -= nums[l]
                l+=1
            ans = max(ans,r-l+1)

        return ans        
