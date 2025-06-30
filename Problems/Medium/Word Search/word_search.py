class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        rows,cols = len(board),len(board[0])

        def backtrack(r,c,idx,seen):
            if idx == len(word):
                return True
            
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != word[idx] or (r,c) in seen:
                return False
            
            seen.add((r,c))
            res = ( backtrack(r+1,c,idx+1,seen) or 
                    backtrack(r-1,c,idx+1,seen) or 
                    backtrack(r,c+1,idx+1,seen) or 
                    backtrack(r,c-1,idx+1,seen)
                  )
            seen.remove((r,c))
            return res
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0,set()):
                        return True
        
        return False

            

        
