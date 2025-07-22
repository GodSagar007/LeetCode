class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i != m-1 and j == n-1:
                    grid[i][j] += grid[i+1][j]
                elif j != n-1 and i == m-1:
                    grid[i][j] += grid[i][j+1]
                elif i != m-1 and j != n-1:
                    grid[i][j] += min(grid[i+1][j],grid[i][j+1])
        
        return grid[0][0]
            
