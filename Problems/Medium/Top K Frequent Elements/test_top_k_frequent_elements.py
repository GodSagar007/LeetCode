import pytest
from typing import List
from collections import Counter
import heapq

# ✅ Solution (in same file)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result[::-1]  # Optional: reverse for higher-to-lower freq

# ✅ Test cases with hardcoded expected top-k elements (any order)
@pytest.mark.parametrize("nums, k, expected", [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),       # 1:3, 2:2 → top 2 are 1 and 2
    ([1], 1, [1]),                         # Single element
    ([1, 1, 1, 2, 2, 3], 1, [1]),          # Top 1 is 1
    ([5, 5, 5, 4, 4, 3], 2, [5, 4]),       # 5:3, 4:2
    ([0, 0, 0, 1, 2, 3], 1, [0]),          # Top 1 is 0
    ([4, 4, 4, 4, 5, 5, 5, 6, 6, 7], 3, [4, 5, 6]),  # 4:4, 5:3, 6:2
    ([-1, -1, 2, 2, 2], 2, [2, -1]),       # 2:3, -1:2
])
def test_top_k_frequent(nums, k, expected):
    sol = Solution()
    output = sol.topKFrequent(nums, k)

    # ✅ Check length
    assert len(output) == len(expected), f"Expected length {len(expected)}, got {len(output)}"

    # ✅ Check that elements match, regardless of order
    assert set(output) == set(expected), f"Expected elements {expected}, got {output}"
