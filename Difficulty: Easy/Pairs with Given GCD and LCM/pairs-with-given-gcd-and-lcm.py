class Solution:
    def pairCount(self, x, y):
        # LCM must be divisible by GCD
        if y % x != 0:
            return 0

        k = y // x

        # Find all pairs (m, n) where m * n = k and gcd(m, n) = 1
        import math
        count = 0

        for m in range(1, int(math.sqrt(k)) + 1):
            if k % m == 0:
                n = k // m
                if math.gcd(m, n) == 1:
                    if m == n:
                        count += 1  # (a, b) where a = b
                    else:
                        count += 2  # (a, b) and (b, a)

        return count