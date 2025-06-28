# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(l1,l2):
            if not l1:
                return l2
            if not l2:
                return l1
            
            if l1.val <l2.val:
                l1.next = merge2Lists(l1.next,l2)
                return l1
            else:
                l2.next = merge2Lists(l2.next,l1)
                return l2
        
        def divideAndConquer(lists,left,right):
            if left == right:
                return lists[(left+right)//2] # Can use any left/right just wanted to be impartial :)
            mid = (left+right)//2
            l1 = divideAndConquer(lists,left,mid)
            l2 = divideAndConquer(lists,mid+1,right)
            return merge2Lists(l1,l2)
        
        if not lists:
            return None
        
        return divideAndConquer(lists,0,len(lists)-1)

                
        
