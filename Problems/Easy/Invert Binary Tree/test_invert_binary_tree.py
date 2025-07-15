import pytest
from typing import Optional

# ✅ Actual solution code
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # For comparison in tests
    def __eq__(self, other):
        if not other:
            return False
        return (
            self.val == other.val and
            self.left == other.left and
            self.right == other.right
        )

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

# ✅ Helper functions
def tree_from_list(lst):
    """Convert level-order list to binary tree."""
    if not lst:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def tree_to_list(root):
    """Convert binary tree to level-order list."""
    if not root:
        return []
    from collections import deque
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

# ✅ Test cases
@pytest.mark.parametrize("input_tree, expected_output", [
    ([], []),
    ([1], [1]),
    ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
    ([1,2,None,3], [1,None,2,None,3]),
    ([1,2,None,3,None], [1,None,2,None,3]),
    ([1,None,2,None,3], [1,2,None,3]),
])
def test_invert_tree(input_tree, expected_output):
    sol = Solution()
    root = tree_from_list(input_tree)
    inverted = sol.invertTree(root)
    assert tree_to_list(inverted) == expected_output
