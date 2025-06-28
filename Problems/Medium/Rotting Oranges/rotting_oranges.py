class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        fresh,t = 0,0
        q = deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i,j])
        
        def isValid(x,y):
            return x>=0 and x<m and y>=0 and y<n and grid[x][y] == 1

        while q and fresh>0:
            size = len(q)
            for k in range(size):
                x,y = q.popleft()
                for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                    X,Y = x+dx,y+dy
                    if isValid(X,Y):
                        grid[X][Y] = 2
                        q.append([X,Y])
                        fresh-=1
            t+=1
        
        return t if fresh == 0 else -1
        
