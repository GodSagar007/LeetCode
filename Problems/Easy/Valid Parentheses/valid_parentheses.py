class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {"(":")","[":"]","{":"}"}

        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            else:
                if not stack or pair[stack.pop()] != bracket:
                    return False
        
        return not stack
                

        
