class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def backtrack(oc,cc,path):
            if len(path) == 2*n:
                output.append(path[:])
                return
            if oc < n:
                backtrack(oc+1,cc,path+'(')
            if cc < oc:
                backtrack(oc,cc+1,path+')')

        backtrack(0,0,"")
        return output 
