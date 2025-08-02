from typing import Optional, List
import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            local_max = node.val + left + right
            self.max = max(self.max, local_max)
            return node.val + max(left, right)

        dfs(root)
        return self.max

# Helper function to build a binary tree from level order list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

@pytest.mark.parametrize(
    "tree_list, expected",
    [
        ([1, 2, 3], 6),                          # 1 + 2 + 3
        ([-10, 9, 20, None, None, 15, 7], 42),   # 15 + 20 + 7
        ([2, -1], 2),                           # Only path with root
        ([1, -2, -3, 1, 3, -2, None, -1], 3),   # Max path: 3 -> -2 -> 1
        ([1], 1),                                # Single node
        ([1, 2], 3),                             # 1 + 2
        ([-3], -3),                              # Single negative node
        ([9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6], 16),  # Complex
    ]
)
def test_maxPathSum(tree_list, expected):
    root = build_tree(tree_list)
    assert Solution().maxPathSum(root) == expected
