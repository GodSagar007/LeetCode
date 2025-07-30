import math
from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        count = 0
        total_ops = len(operations)
        
        while k != 1:
            jump = math.ceil(math.log2(k))
            idx = jump - 1
            if idx >= total_ops:
                idx = total_ops - 1
            count += operations[idx]
            k -= 2**(jump - 1)
        
        count %= 26
        return chr(97 + count)
