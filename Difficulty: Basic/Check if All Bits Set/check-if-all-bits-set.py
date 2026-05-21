class Solution:
    def isBitSet(self, n):
        # 0 is not considered as all bits set
        if n == 0:
            return False
        
        # Check if n is of form 2^k - 1
        return (n & (n + 1)) == 0