class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 -1
        sign = [1,-1][x<0]
        x = abs(x)
        ans = 0

        while x:
            x,rem = divmod(x,10)
            ans = ans*10 + rem
            if ans > MAX:
                return 0
        return sign *ans
