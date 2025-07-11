class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumps,farthest,currEnd = 0,0,0
        for i in range(len(nums)-1):
            farthest = max(farthest,i+nums[i])
            if i == currEnd:
                minJumps+=1
                currEnd = farthest
        return minJumps
        



