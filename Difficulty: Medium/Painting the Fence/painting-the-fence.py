class Solution:
    def countWays(self, n, k):
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        mod = 1000000007
        
        same = k * 1
        diff = k * (k - 1)
        
        for i in range(3, n + 1):
            new_same = diff * 1
            new_diff = (same + diff) * (k - 1)
            same, diff = new_same % mod, new_diff % mod
        
        return (same + diff) % mod