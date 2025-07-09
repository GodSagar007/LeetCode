class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = str(x)
        return True if l == l[::-1] else False
        
