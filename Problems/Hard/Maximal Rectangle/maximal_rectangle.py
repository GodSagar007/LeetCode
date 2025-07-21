from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        height = [0] * cols
        best = 0

        for r in range(rows):
            for c in range(cols):
                height[c] = height[c] + 1 if matrix[r][c] == '1' else 0

            stack = []                      
            for i in range(cols + 1):       
                cur_h = height[i] if i < cols else 0
                while stack and cur_h < height[stack[-1]]:
                    h = height[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    best = max(best, h * width)
                stack.append(i)

        return best
