import pytest
from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        schedule = []

        while q:
            course = q.popleft()
            schedule.append(course)
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return len(schedule) == numCourses


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize("numCourses, prerequisites, expected", [
    # ✅ Basic linear dependency
    (2, [[1, 0]], True),                # Can finish course 0 → then 1

    # ❌ Cycle
    (2, [[0, 1], [1, 0]], False),       # 0 → 1 → 0

    # ✅ Diamond structure
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),

    # ❌ Cycle in diamond
    (4, [[1, 0], [2, 0], [3, 1], [3, 2], [1, 3]], False),

    # ✅ Disconnected components (valid)
    (5, [[1, 0], [3, 2]], True),

    # ❌ Self dependency
    (1, [[0, 0]], False),

    # ✅ No prerequisites
    (3, [], True),

    # ✅ One course, no prerequisites
    (1, [], True),

    # ✅ Larger acyclic graph
    (6, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]], True),

    # ❌ Larger cyclic graph
    (6, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [0, 5]], False)
])
def test_can_finish(sol, numCourses, prerequisites, expected):
    assert sol.canFinish(numCourses, prerequisites) == expected
