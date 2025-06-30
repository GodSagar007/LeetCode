import pytest
from collections import defaultdict, deque
from typing import List


# Your original solution
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

        return schedule if len(schedule) == numCourses else []


# Helper to validate topological order
def is_valid_topo_order(order, prerequisites):
    position = {course: idx for idx, course in enumerate(order)}
    for a, b in prerequisites:
        if position[a] < position[b]:  # a comes before b → invalid
            return False
    return True


# Helper to detect if a cycle exists
def has_cycle(numCourses, prerequisites):
    graph = defaultdict(list)
    visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

    def dfs(u):
        if visited[u] == 1:
            return True
        if visited[u] == 2:
            return False
        visited[u] = 1
        for v in graph[u]:
            if dfs(v):
                return True
        visited[u] = 2
        return False

    for a, b in prerequisites:
        graph[b].append(a)
    for i in range(numCourses):
        if dfs(i):
            return True
    return False


@pytest.fixture
def sol():
    return Solution()


@pytest.mark.parametrize("numCourses, prerequisites", [
    (2, [[1, 0]]),                       # simple linear
    (4, []),                             # no prerequisites
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),  # diamond shape
    (2, [[0, 1], [1, 0]]),              # cycle
    (4, [[1, 0], [3, 2]]),              # disconnected graph
    (3, [[1, 0], [0, 2], [2, 1]]),      # cycle
    (1, []),                             # one course
    (2, []),                             # two courses, no prerequisites
    (3, [[1, 0], [2, 1]]),              # chain
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),  # diamond again
])
def test_find_order(sol, numCourses, prerequisites):
    result = sol.findOrder(numCourses, prerequisites)
    if not result:
        assert has_cycle(numCourses, prerequisites), f"Expected cycle but got empty result: {result}"
    else:
        assert len(result) == numCourses, f"Length mismatch: got {len(result)}, expected {numCourses}"
        assert set(result) == set(range(numCourses)), f"Invalid elements: {result}"
        assert is_valid_topo_order(result, prerequisites), f"Not a valid topo order: {result}"
