import pytest
from heapq import heappush, heappop
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        intervals.sort(key = lambda x: x[0])

        for interval in intervals:
            if rooms and interval[0] >= rooms[0]:
                heappop(rooms)
            heappush(rooms, interval[1])

        return len(rooms)

@pytest.mark.parametrize("intervals, expected", [
    # 🧪 Single meeting
    ([[0, 30]], 1),

    # 🧪 Non-overlapping meetings
    ([[0, 10], [15, 25], [30, 40]], 1),

    # 🧪 Completely overlapping meetings
    ([[0, 30], [5, 10], [15, 20]], 2),

    # 🧪 All meetings at same time
    ([[1, 10], [1, 10], [1, 10]], 3),

    # 🧪 Meetings with partial overlap
    ([[1, 5], [2, 6], [8, 9]], 2),

    # 🧪 Meetings starting when others end
    ([[0, 10], [10, 20], [20, 30]], 1),

    # 🧪 Empty input
    ([], 0),

    # 🧪 Complex mix
    ([[0,30],[5,10],[15,20],[35,40],[38,45],[10,15]], 3),

    # 🧪 Nested meetings
    ([[1, 100], [10, 20], [30, 40], [50, 60]], 2),

    # 🧪 Long meeting and short ones
    ([[1, 100], [2, 3], [4, 5], [6, 7], [8, 9]], 2),
])
def test_min_meeting_rooms(intervals, expected):
    sol = Solution()
    assert sol.minMeetingRooms(intervals) == expected
