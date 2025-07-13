class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R,C = len(matrix),len(matrix[0])
        start,end = 0,R*C-1
        while start<=end:
            mid = (end+start)//2
            r,c = mid//C,mid%C
            if matrix[r][c] == target:
                return True
            elif matrix[r][c]<target:
                start = mid+1
            else:
                end = mid-1
        return False
        
