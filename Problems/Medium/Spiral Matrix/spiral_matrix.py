class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rs, cs = 0, 0
        re, ce = len(matrix) - 1, len(matrix[0]) - 1
        ans = []
        
        while rs <= re and cs <= ce:
            # Left to Right
            for c in range(cs, ce + 1):
                ans.append(matrix[rs][c])
            rs += 1
            
            # Top to Bottom
            for r in range(rs, re + 1):
                ans.append(matrix[r][ce])
            ce -= 1
            
            if rs <= re:
                # Right to Left
                for c in range(ce, cs - 1, -1):
                    ans.append(matrix[re][c])
                re -= 1
            
            if cs <= ce:
                # Bottom to Top
                for r in range(re, rs - 1, -1):
                    ans.append(matrix[r][cs])
                cs += 1
        
        return ans
