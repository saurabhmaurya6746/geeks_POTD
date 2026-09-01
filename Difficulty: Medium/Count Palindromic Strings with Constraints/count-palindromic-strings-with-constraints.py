class Solution:
    def palindromicStrings(self, n, k):
        MOD = 10**9 + 7
    
        def nCr(n, r):
            """Calculate combination nCr"""
            if r > n or r < 0:
                return 0
            if r == 0 or r == n:
                return 1
            # Use multiplicative formula
            result = 1
            for i in range(r):
                result = (result * (n - i)) % MOD
                result = (result * pow(i + 1, MOD - 2, MOD)) % MOD
            return result
    
        def factorial(num):
            """Calculate factorial of num"""
            result = 1
            for i in range(1, num + 1):
                result = (result * i) % MOD
            return result
    
        total = 0
    
        # For even lengths: 2, 4, 6, ..., 2*floor(n/2)
        for length in range(2, n + 1, 2):
            m = length // 2  # number of pairs needed
            if m <= k:
                # Choose m characters from k to appear twice
                # Arrange them in m! ways (positions of pairs)
                ways = nCr(k, m) * factorial(m) % MOD
                total = (total + ways) % MOD
    
        # For odd lengths: 1, 3, 5, ..., 2*floor((n-1)/2) + 1
        for length in range(1, n + 1, 2):
            m = length // 2  # number of pairs needed
            if m <= k - 1:  # need at least one character left for center
                # Choose m characters for pairs from k
                # Choose 1 character for center from remaining (k - m)
                # Arrange the m pairs in m! ways
                ways = nCr(k, m) * (k - m) % MOD * factorial(m) % MOD
                total = (total + ways) % MOD
    
        return total