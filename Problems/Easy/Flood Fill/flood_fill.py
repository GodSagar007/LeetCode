class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0] or image[sr][sc] == color:
            return image
        def dfs(x,y,org,new):
            if x<0 or x == len(image) or y<0 or y == len(image[0]) or image[x][y] != org:
                return
            image[x][y] = new
            dfs(x+1,y,org,new)
            dfs(x,y+1,org,new)
            dfs(x-1,y,org,new)
            dfs(x,y-1,org,new)
        
        dfs(sr,sc,image[sr][sc],color)
        
        return image
