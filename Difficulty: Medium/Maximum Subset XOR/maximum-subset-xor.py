class Solution:
    def maxSubsetXOR(self, arr):
        # Initialize basis array for 31 bits (since arr[i] <= 10^6 < 2^20)
        # Using 31 bits to be safe
        basis = [0] * 31
        
        # Build the linear basis
        for x in arr:
            y = x
            # Process from most significant bit to least
            for i in range(30, -1, -1):
                # Check if bit i is set in y
                if (y >> i) & 1:
                    # If basis[i] is empty, store y and break
                    if basis[i] == 0:
                        basis[i] = y
                        break
                    else:
                        # XOR with basis[i] to reduce y
                        y ^= basis[i]
        
        # Find the maximum XOR value
        ans = 0
        for i in range(30, -1, -1):
            # Greedily take basis vectors to maximize the result
            if (ans ^ basis[i]) > ans:
                ans ^= basis[i]
        
        return ans