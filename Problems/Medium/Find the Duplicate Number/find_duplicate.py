class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = nums[0],nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slowAgain = nums[0]
        while slowAgain != fast:
            slowAgain = nums[slowAgain]
            fast = nums[fast]
        
        return slowAgain
