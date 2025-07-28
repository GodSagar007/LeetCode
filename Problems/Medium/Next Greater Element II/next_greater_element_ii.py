class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in reversed(range(2*n-1)):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if stack and i<n:
                result[i] = stack[-1]
            stack.append(nums[i%n])

        return result        
