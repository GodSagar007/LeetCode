class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right = -1,-1
        def findLeft():
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        def findRight():
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high

        left = findLeft()
        right = findRight()

        if left <= right and left < len(nums) and nums[left] == target:
            return [left, right]
        else:
            return [-1, -1]
