import pytest
from collections import defaultdict
from typing import List

# Your solution (assumed in same file)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        components = 0
        seen = set()

        def dfs(node):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)

        for i in range(n):
            if i not in seen:
                components += 1
                dfs(i)

        return components

# ---------- Pytest test cases ----------
@pytest.mark.parametrize("n, edges, expected", [
    (5, [[0,1],[1,2],[3,4]], 2),  # 2 components: [0-1-2], [3-4]
    (5, [[0,1],[1,2],[2,3],[3,4]], 1),  # fully connected
    (5, [], 5),  # no edges, each node is its own component
    (1, [], 1),  # single node
    (2, [[1,0]], 1),  # two nodes connected
    (4, [[0,1],[2,3]], 2),  # two separate edges
    (4, [[0,1],[1,2],[2,0]], 2),  # one triangle and one isolated node
    (6, [[0,1],[1,2],[3,4],[4,5]], 2),  # two chains
    (0, [], 0),  # no nodes
])
def test_count_components(n, edges, expected):
    sol = Solution()
    assert sol.countComponents(n, edges) == expected
