class Solution:
    def bitonic(self, arr):
        n = len(arr)
        if n == 0:
            return 0
            
        # Increasing and Decreasing arrays initialized with 1
        inc = [1] * n
        dec = [1] * n
        
        # Step 1: Fill the inc array from left to right
        for i in range(1, n):
            if arr[i] >= arr[i - 1]:
                inc[i] = inc[i - 1] + 1
                
        # Step 2: Fill the dec array from right to left
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                dec[i] = dec[i + 1] + 1
                
        # Step 3: Find the maximum length
        max_len = 0
        for i in range(n):
            max_len = max(max_len, inc[i] + dec[i] - 1)
            
        return max_len