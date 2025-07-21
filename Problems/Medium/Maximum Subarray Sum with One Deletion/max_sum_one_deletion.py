from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        no_del = arr[0]
        one_del = float('-inf')
        max_sum = no_del

        for i in range(1,n):
            one_del = max(one_del+arr[i],no_del)
            no_del = max(no_del+arr[i],arr[i])
            max_sum = max(max_sum,no_del,one_del)
        
        return max_sum
