import pytest
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Your original implementation
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l1.next = merge2Lists(l1.next, l2)
                return l1
            else:
                l2.next = merge2Lists(l2.next, l1)
                return l2

        def divideAndConquer(lists, left, right):
            if left == right:
                return lists[left]
            mid = (left + right) // 2
            l1 = divideAndConquer(lists, left, mid)
            l2 = divideAndConquer(lists, mid + 1, right)
            return merge2Lists(l1, l2)

        if not lists:
            return None

        return divideAndConquer(lists, 0, len(lists) - 1)

# Helpers
def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def list_to_array(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

@pytest.fixture
def sol():
    return Solution()

@pytest.mark.parametrize(
    "lists, expected",
    [
        # Basic case
        ([[1,4,5], [1,3,4], [2,6]], [1,1,2,3,4,4,5,6]),

        # All lists empty
        ([[], [], []], []),

        # Some empty, some not
        ([[], [1], []], [1]),

        # Only one list
        ([[1,2,3]], [1,2,3]),

        # Two sorted lists
        ([[1,3,5], [2,4,6]], [1,2,3,4,5,6]),

        # Overlapping values
        ([[1,1,1], [1,1], [1]], [1,1,1,1,1,1]),

        # Negative numbers
        ([[-10,-5,0], [-6,-3,1], [-2,2,3]], [-10,-6,-5,-3,-2,0,1,2,3]),

        # Single long list vs several small
        ([[1,3,5,7,9], [2], [4], [6], [8], [10]], [1,2,3,4,5,6,7,8,9,10]),

        # One list only
        ([[]], []),
    ]
)
def test_merge_k_lists(sol, lists, expected):
    list_nodes = [build_linked_list(l) for l in lists]
    result = sol.mergeKLists(list_nodes)
    assert list_to_array(result) == expected
