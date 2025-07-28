from collections import defaultdict, deque
from typing import List
import pytest

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color = [0] * (n + 1)
        for person in range(1, n + 1):
            if color[person] != 0:
                continue
            
            q = deque([person])
            color[person] = 1
            while q:
                person = q.popleft()
                for hater in graph[person]:
                    if color[hater] == color[person]:
                        return False
                    if color[hater] == 0:
                        color[hater] = -color[person]
                        q.append(hater)

        return True

@pytest.mark.parametrize(
    "n, dislikes, expected",
    [
        (4, [[1,2],[1,3],[2,4]], True),
        (3, [[1,2],[1,3],[2,3]], False),
        (5, [[1,2],[2,3],[3,4],[4,5],[1,5]], False),
        (10, [], True),
        (1, [], True),
        (2, [[1,2]], True),
        (3, [[1,2],[2,3],[1,3]], False),
        (6, [[1,2],[2,3],[3,4],[4,5],[5,6],[6,1]], False),  # cycle of odd length
        (6, [[1,2],[2,3],[3,4],[4,5],[5,6]], True),         # chain
    ]
)
def test_possible_bipartition(n, dislikes, expected):
    assert Solution().possibleBipartition(n, dislikes) == expected
