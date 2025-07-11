class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans,seen = 0,defaultdict(int)
        seen[0] = 1

        prefixsum = 0
        for num in nums:
            prefixsum += num
            if prefixsum - k in seen:
                ans += seen[prefixsum - k]
            seen[prefixsum]+=1
        return ans
