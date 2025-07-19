from typing import Optional, List
from collections import deque
import pytest

# -------------- TreeNode definition --------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -------------- Solution class -------------------
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result

# --------- Helper to build tree from list --------
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    q = deque([root])
    for v in it:
        parent = q[0]
        node = TreeNode(v) if v is not None else None
        if not parent.left:
            parent.left = node
        elif not parent.right:
            parent.right = node
            q.popleft()
        if node:
            q.append(node)
    return root

# -------------- Test Suite -----------------------
@pytest.mark.parametrize(
    "values, expected",
    [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
    ([1, 2, 3, 4], [1, 3, 4]),
    ([1, None, 2, None, 3], [1, 2, 3]),
    ([1, 2, None, 3, None, 4, None], [1, 2, 3, 4]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3, 7, 9]),
    ([i for i in range(1, 101)], [1, 3, 7, 15, 31, 63, 100]),
]
,
)
def test_right_side_view(values, expected):
    root = build_tree(values)
    assert Solution().rightSideView(root) == expected
