from typing import List
from collections import defaultdict
import unittest

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))
        
        def dfs(curr, target, seen, val):
            if curr not in graph or target not in graph:
                return -1.0
            if curr == target:
                return val
            seen.add(curr)
            for neighbor, weight in graph[curr]:
                if neighbor not in seen:
                    result = dfs(neighbor, target, seen, val * weight)
                    if result != -1:
                        return result
            return -1.0

        results = []
        for c, d in queries:
            results.append(dfs(c, d, set(), 1))
        return results


class TestCalcEquation(unittest.TestCase):

    def test_examples(self):
        sol = Solution()
        self.assertAlmostEqual(sol.calcEquation(
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        ), [6.0, 0.5, -1.0, 1.0, -1.0], places=5)

    def test_large_chain(self):
        sol = Solution()
        self.assertAlmostEqual(sol.calcEquation(
            [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
            [3.0, 4.0, 5.0, 6.0],
            [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]
        ), [360.0, 1/120.0, 20.0, 1.0, -1.0, -1.0], places=5)

    def test_single_equation(self):
        sol = Solution()
        self.assertEqual(sol.calcEquation(
            [["a", "b"]],
            [4.0],
            [["a", "b"], ["b", "a"], ["a", "a"], ["b", "b"], ["a", "c"], ["x", "x"]]
        ), [4.0, 0.25, 1.0, 1.0, -1.0, -1.0])

    def test_cycle(self):
        sol = Solution()
        self.assertAlmostEqual(sol.calcEquation(
            [["a", "b"], ["b", "c"], ["c", "a"]],
            [2.0, 3.0, 0.5],
            [["a", "c"], ["c", "b"], ["b", "a"]]
        ), [6.0, 1/3.0, 0.5], places=5)

    def test_disconnected(self):
        sol = Solution()
        self.assertEqual(sol.calcEquation(
            [["a", "b"], ["c", "d"]],
            [2.0, 3.0],
            [["a", "d"], ["b", "c"]]
        ), [-1.0, -1.0])


if __name__ == "__main__":
    unittest.main()
