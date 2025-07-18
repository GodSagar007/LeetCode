class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in reversed(range(len(nums))):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
        
