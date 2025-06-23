class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx,num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [idx,seen[complement]]
            seen[num] = idx
            
        return [None,None]
