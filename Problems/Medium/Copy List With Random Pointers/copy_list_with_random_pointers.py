"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        # Create Clones with values
        curr = head
        while curr:
            clone = Node(curr.val)
            clone.next = curr.next
            curr.next = clone
            curr = clone.next
        
        # Point the Random Pointers of Clones
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next 
            curr = curr.next.next
        
        # Seprate Clones from Original List
        curr = head
        cloneHead = head.next
        
        while curr:
            clone = curr.next
            curr.next = clone.next
            if clone.next:
                clone.next = clone.next.next
            curr = curr.next
        
        return cloneHead
