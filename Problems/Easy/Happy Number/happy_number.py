class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            summ = 0
            while n>0:
                n,digit = divmod(n,10)
                summ+=digit**2
            return summ

        slow = n
        fast = n
        
        while fast!=1:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            if slow == fast:
                break
        
        return fast == 1

