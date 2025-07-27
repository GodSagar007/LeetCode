class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me,count = None,0
        for num in nums:
            if num == me:
                count+=1
            else:
                if count == 0:
                    me = num
                    count = 1
                else:
                    count-=1
        return me
        
        
