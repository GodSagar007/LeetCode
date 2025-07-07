from typing import List
import pytest
import heapq

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])

        maxProfit = 0
        heap = []

        for s, e, p in jobs:
            while heap and heap[0][0] <= s:
                _, prof = heapq.heappop(heap)
                maxProfit = max(maxProfit, prof)

            heapq.heappush(heap, (e, maxProfit + p))

        while heap:
            _, prof = heapq.heappop(heap)
            maxProfit = max(maxProfit, prof)

        return maxProfit


@pytest.mark.parametrize("startTime, endTime, profit, expected", [
    # Basic non-overlapping jobs
    ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], 18),

    # Overlapping jobs, best to skip some
    ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120),

    # Nested jobs (one inside another)
    ([1, 2, 3], [10, 4, 5], [20, 50, 60], 60),

    # All jobs overlap, pick best one
    ([1, 1, 1], [3, 3, 3], [20, 50, 10], 50),

    # Jobs with same start time but different profits
    ([1, 1, 1], [2, 3, 4], [5, 10, 15], 15),

    # Jobs with gaps between them
    ([1, 10, 20], [5, 15, 25], [10, 20, 30], 60),

    # Single job
    ([5], [10], [100], 100),

    # Zero-profit jobs
    ([1, 2, 3], [2, 3, 4], [0, 0, 0], 0),

    # Tight overlapping jobs, greedy won't work
    ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150),

    # Large input with non-overlapping optimal path
    ([1, 3, 6, 2], [2, 5, 19, 100], [50, 20, 100, 200], 250),
])
def test_jobScheduling(startTime: List[int], endTime: List[int], profit: List[int], expected: int):
    s = Solution()
    assert s.jobScheduling(startTime, endTime, profit) == expected
