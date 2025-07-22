# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = defaultdict(list)
        def dfs(node,row,col):
            if not node:
                return
            heapq.heappush(values[col],(row,node.val))
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
        dfs(root,0,0)
        result = []
        for col in sorted(values.keys()):
            row = []
            while values[col]:
                row.append(heapq.heappop(values[col])[1])
            result.append(row)
        return result
        
