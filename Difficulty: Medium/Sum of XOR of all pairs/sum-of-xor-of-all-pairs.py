class Solution:
    def sumXOR(self, arr):
        n = len(arr)
        total = 0
        
        # Check each bit position
        for bit in range(32):
            count_set = 0
            for num in arr:
                if num & (1 << bit):
                    count_set += 1
            count_unset = n - count_set
            # Each pair with different bits contributes (1 << bit) to XOR
            total += count_set * count_unset * (1 << bit)
        
        return total