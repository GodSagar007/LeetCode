class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        maxArea = 0
        def dfs(x,y):
            if x<0 or x == m or y<0 or y == n or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return 1 + dfs(x+1,y) + dfs(x-1,y) + dfs(x,y-1) + dfs(x,y+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    maxArea = max(maxArea,area)
        
        return maxArea
        
