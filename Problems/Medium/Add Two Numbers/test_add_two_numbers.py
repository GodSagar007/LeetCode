import pytest
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution class with addTwoNumbers method
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sentinel = ListNode(-1)
        head = sentinel 

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            head.next = ListNode(carry % 10)
            head = head.next
            carry //= 10

        return sentinel.next 

# Helper: Convert list to linked list
def list_to_linked(lst: List[int]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

# Helper: Convert linked list to list
def linked_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases
@pytest.mark.parametrize("l1, l2, expected", [
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),         # 342 + 465 = 807
    ([1, 8], [0], [1, 8]),                     # 81 + 0 = 81
    ([9, 9], [1], [0, 0, 1]),                  # 99 + 1 = 100
    ([9, 9, 9], [9, 9, 9], [8, 9, 9, 1]),      # 999 + 999 = 1998
    ([2, 4], [5, 6, 7], [7, 0, 8]),            # 42 + 765 = 807
    ([0], [0], [0]),                           # 0 + 0 = 0
    ([5], [5], [0, 1]),                        # 5 + 5 = 10
    ([1], [9, 9, 9], [0, 0, 0, 1])             # 1 + 999 = 1000
])
def test_add_two_numbers(l1, l2, expected):
    sol = Solution()
    l1_node = list_to_linked(l1)
    l2_node = list_to_linked(l2)
    result_node = sol.addTwoNumbers(l1_node, l2_node)
    result_list = linked_to_list(result_node)
    assert result_list == expected, f"Expected {expected}, but got {result_list}"
