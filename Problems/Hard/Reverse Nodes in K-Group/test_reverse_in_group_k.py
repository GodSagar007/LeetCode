import pytest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev = groupNext
            curr = groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

@pytest.mark.parametrize("input_list,k,expected", [
    ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
    ([1, 2], 2, [2, 1]),
    ([1, 2], 3, [1, 2]),
    ([], 2, []),
    ([7, 7, 7, 7], 2, [7, 7, 7, 7]),
    ([1, 2, 3, 4, 5, 6], 6, [6, 5, 4, 3, 2, 1]),
])
def test_reverseKGroup(input_list, k, expected):
    sol = Solution()
    head = list_to_linkedlist(input_list)
    result_head = sol.reverseKGroup(head, k)
    result_list = linkedlist_to_list(result_head)
    assert result_list == expected
