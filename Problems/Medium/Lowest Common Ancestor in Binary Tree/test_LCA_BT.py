import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right

# 🔧 Helper to build tree by dictionary path
def build_tree():
    # Building this tree:
    #         3
    #       /   \
    #      5     1
    #     / \   / \
    #    6   2 0   8
    #       / \
    #      7   4

    nodes = {i: TreeNode(i) for i in range(9)}
    nodes[3].left = nodes[5]
    nodes[3].right = nodes[1]
    nodes[5].left = nodes[6]
    nodes[5].right = nodes[2]
    nodes[1].left = nodes[0]
    nodes[1].right = nodes[8]
    nodes[2].left = nodes[7]
    nodes[2].right = nodes[4]
    return nodes

@pytest.mark.parametrize(
    "p_val, q_val, expected_val",
    [
        (5, 1, 3),      # LCA of 5 and 1 is 3
        (6, 4, 5),      # LCA of 6 and 4 is 5
        (7, 8, 3),      # LCA of 7 and 8 is 3
        (7, 2, 2),      # LCA of 7 and 2 is 2 (one is parent of the other)
        (0, 8, 1),      # LCA of 0 and 8 is 1
        (5, 4, 5),      # 5 is ancestor of 4
        (3, 4, 3),      # root and descendant
    ]
)
def test_lowest_common_ancestor(p_val, q_val, expected_val):
    nodes = build_tree()
    root = nodes[3]
    sol = Solution()
    p = nodes[p_val]
    q = nodes[q_val]
    result = sol.lowestCommonAncestor(root, p, q)
    assert result.val == expected_val
