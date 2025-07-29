import pytest
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        is_prime = [False, False] + [True] * (n - 2)

        for i in range(2, math.isqrt(n) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),               # No primes
        (1, 0),               # No primes
        (2, 0),               # Edge case, primes < 2
        (3, 1),               # Only prime is 2
        (10, 4),              # 2, 3, 5, 7
        (20, 8),              # 2, 3, 5, 7, 11, 13, 17, 19
        (100, 25),            # Known count of primes < 100
        (499979, 41537),      # Stress test (expected count verified)
    ]
)
def test_count_primes(n, expected):
    assert Solution().countPrimes(n) == expected
