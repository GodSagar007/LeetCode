import pytest
from typing import Optional

# ------------------- Node & Solution -------------------
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # 1. Clone nodes and interleave
        curr = head
        while curr:
            clone = Node(curr.val)
            clone.next = curr.next
            curr.next = clone
            curr = clone.next

        # 2. Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 3. Separate the two lists
        curr = head
        clone_head = head.next
        while curr:
            clone = curr.next
            curr.next = clone.next
            if clone.next:
                clone.next = clone.next.next
            curr = curr.next

        return clone_head
# --------------------------------------------------------


# -------------------- Test Utilities --------------------
def build_linked_list_with_randoms(values, random_indices):
    """values: list of node values
       random_indices: list of indices for random pointers (or None)
    """
    nodes = [Node(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, rand_idx in enumerate(random_indices):
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0] if nodes else None

def extract_list(head):
    """Returns list of (val, random_index) for verification"""
    node_to_idx = {}
    nodes = []
    curr = head
    i = 0
    while curr:
        node_to_idx[curr] = i
        nodes.append(curr)
        curr = curr.next
        i += 1
    result = []
    for node in nodes:
        rand_idx = node_to_idx.get(node.random) if node.random else None
        result.append((node.val, rand_idx))
    return result
# --------------------------------------------------------


# ----------------------- Tests --------------------------
@pytest.mark.parametrize("values, randoms", [
    ([7, 13, 11, 10, 1], [None, 0, 4, 2, 0]),         # LeetCode-style test
    ([1, 2], [1, 1]),                                 # Two nodes pointing to each other
    ([3, 3, 3], [None, 0, None]),                     # Duplicates with partial randoms
    ([1], [0]),                                       # Single node pointing to itself
    ([], []),                                         # Empty list
])
def test_copy_random_list(values, randoms):
    original = build_linked_list_with_randoms(values, randoms)
    copied = Solution().copyRandomList(original)

    assert extract_list(copied) == extract_list(build_linked_list_with_randoms(values, randoms))
# --------------------------------------------------------
