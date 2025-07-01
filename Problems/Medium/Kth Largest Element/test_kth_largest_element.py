import pytest
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]

@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # 🔹 Basic Cases
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
        ([1], 1, 1),

        # 🔹 Edge Cases
        ([5,5,5,5,5], 3, 5),                # all elements same
        (list(range(1, 10001)), 1, 10000),  # large input, max element
        ([7,6,5,4,3,2,1], 7, 1),            # k == len(nums)
        ([2,1], 2, 1),                      # small array

        # 🔹 Negative numbers
        ([-1,-2,-3,-4,-5], 2, -2),
        ([0, -1, 1], 2, 0),

        # 🔹 Duplicates and extremes
        ([1, 2, 2, 3, 3, 4, 4], 5, 2),
        ([100, -100, 0, 50, 50], 3, 50),
    ]
)
def test_find_kth_largest(nums, k, expected):
    sol = Solution()
    assert sol.findKthLargest(nums, k) == expected
