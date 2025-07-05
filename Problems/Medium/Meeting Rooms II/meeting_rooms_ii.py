class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        intervals.sort(key = lambda x: x[0])

        for interval in intervals:
            if rooms and interval[0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms,interval[1])
        
        return len(rooms)


        
