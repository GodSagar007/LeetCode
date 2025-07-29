class Solution:
    def countPrimes(self, n: int) -> int:
        if n<= 2:
            return 0
        
        is_prime = [False,False] + [True]*(n-2)

        for i in range(2,math.isqrt(n)+1):
            if is_prime[i]:
                for j in range(i*i,n,i):
                    is_prime[j] = False

        return sum(is_prime)
