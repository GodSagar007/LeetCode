class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = -1
        for i in reversed(range(len(nums)-1)):
            if nums[i]<nums[i+1]:
                idx = i
                break
        
        if idx == -1:
            nums.sort()
            return
        
        idxSwap = -1
        for i in range(idx+1,len(nums)):
            if nums[idx]<nums[i]:
                idxSwap = i
        
        nums[idx],nums[idxSwap] = nums[idxSwap],nums[idx]
        nums[idx+1:] = sorted(nums[idx+1:])

        


