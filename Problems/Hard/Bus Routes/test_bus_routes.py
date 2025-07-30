from collections import defaultdict, deque
import pytest

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        stop_to_buses = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(i)

        visited_stops = set()
        visited_buses = set()
        queue = deque([(source, 0)])

        while queue:
            stop, buses_taken = queue.popleft()
            if stop == target:
                return buses_taken

            for bus in stop_to_buses[stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)

                for next_stop in routes[bus]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))

        return -1

# ---------------------- Pytest Suite ----------------------

@pytest.mark.parametrize("routes, source, target, expected", [
    ([[1, 2, 7], [3, 6, 7]], 1, 6, 2),
    ([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12, -1),
    ([[1, 2, 3, 4, 5]], 1, 5, 1),
    ([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 1, 7, 3),
    ([[1, 2, 3], [3, 4, 5]], 1, 1, 0),
    ([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 1, 8, -1),
])
def test_num_buses_to_destination(routes, source, target, expected):
    sol = Solution()
    assert sol.numBusesToDestination(routes, source, target) == expected
