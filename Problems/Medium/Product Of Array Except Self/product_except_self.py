class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = 1
        output = [0]*n
        for i in range(n):
            output[i] = pre
            pre*=nums[i]
        post = 1
        for i in reversed(range(n)):
            output[i] *= post
            post*=nums[i]
        
        return output
            
        
