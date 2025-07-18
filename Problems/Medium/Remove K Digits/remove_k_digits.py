class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and stack[-1]>digit and k>0:
                stack.pop()
                k-=1
            stack.append(digit)
        while k>0:
            stack.pop()
            k-=1
        result = "".join(stack).lstrip('0') or '0'
        return result
