class Solution:
    def maxDiffSubArrays(self, arr):
        n = len(arr)
        
        # Left-to-Right DP arrays
        left_max = [0] * n
        left_min = [0] * n
        
        # Right-to-Left DP arrays
        right_max = [0] * n
        right_min = [0] * n
        
        # Fill Left Arrays (Standard Kadane's and its inverted version)
        current_max = arr[0]
        max_so_far = arr[0]
        left_max[0] = arr[0]
        
        current_min = arr[0]
        min_so_far = arr[0]
        left_min[0] = arr[0]
        
        for i in range(1, n):
            current_max = max(arr[i], current_max + arr[i])
            max_so_far = max(max_so_far, current_max)
            left_max[i] = max_so_far
            
            current_min = min(arr[i], current_min + arr[i])
            min_so_far = min(min_so_far, current_min)
            left_min[i] = min_so_far
            
        # Fill Right Arrays
        current_max = arr[n-1]
        max_so_far = arr[n-1]
        right_max[n-1] = arr[n-1]
        
        current_min = arr[n-1]
        min_so_far = arr[n-1]
        right_min[n-1] = arr[n-1]
        
        for i in range(n-2, -1, -1):
            current_max = max(arr[i], current_max + arr[i])
            max_so_far = max(max_so_far, current_max)
            right_max[i] = max_so_far
            
            current_min = min(arr[i], current_min + arr[i])
            min_so_far = min(min_so_far, current_min)
            right_min[i] = min_so_far
            
        # Maximize the absolute difference
        max_diff = float('-inf')
        for i in range(n - 1):
            diff1 = abs(left_max[i] - right_min[i + 1])
            diff2 = abs(left_min[i] - right_max[i + 1])
            max_diff = max(max_diff, diff1, diff2)
            
        return max_diff