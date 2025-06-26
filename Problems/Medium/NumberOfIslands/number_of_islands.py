class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(x,y):
            if x<0 or x == len(grid) or y<0 or y == len(grid[0]) or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)        

        numIslands = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    numIslands += 1
                    dfs(x,y)
        
        return numIslands



        
