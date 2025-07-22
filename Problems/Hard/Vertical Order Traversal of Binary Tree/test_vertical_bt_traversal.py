import heapq
from collections import defaultdict
from typing import List, Optional
import pytest

# ---------------------- TreeNode + Your Code ----------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = defaultdict(list)

        def dfs(node, row, col):
            if not node:
                return
            heapq.heappush(values[col], (row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        result = []
        for col in sorted(values.keys()):
            row = []
            while values[col]:
                row.append(heapq.heappop(values[col])[1])
            result.append(row)

        return result
# ------------------------------------------------------------------


# ----------------------- Tree Builder -----------------------------
def build_tree(values):
    """Builds a binary tree from a list (LeetCode style level order)"""
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root
# ------------------------------------------------------------------


# ------------------------ Pytest Tests ----------------------------
@pytest.mark.parametrize("tree_input, expected", [
    # 1. Single node
    ([1], [[1]]),

    # 2. Left & right subtree example (classic)
    ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),

    # 3. Right-leaning only
    ([1, None, 2, None, 3], [[1], [2], [3]]),

    # 4. Nodes with same (row, col), test value sorting
    ([1, 2, 3, 4, 6, 5, 7], [[4], [2], [1, 5, 6], [3], [7]]),

    # 5. Balanced tree
    ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),

    # 6. Complex overlap case
    ([0, 8, 1, None, None, 3, 2, 4, 5, 4, 4, 6, 7], [[8], [0, 3, 4, 4], [1, 2, 5, 6], [4, 7]]),
])
def test_vertical_traversal(tree_input, expected):
    root = build_tree(tree_input)
    assert Solution().verticalTraversal(root) == expected
# ------------------------------------------------------------------
