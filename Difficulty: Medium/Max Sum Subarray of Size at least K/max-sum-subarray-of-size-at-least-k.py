class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        n = len(arr)
        
        # Step 1: Compute maximum sum subarray ending at each index (Kadane's Algorithm)
        max_sum = [0] * n
        max_sum[0] = arr[0]
        
        for i in range(1, n):
            max_sum[i] = max(arr[i], max_sum[i - 1] + arr[i])
            
        # Step 2: Calculate sum of the first window of size k
        current_sum = sum(arr[:k])
        max_result = current_sum
        
        # Step 3: Slide the window of size k across the array
        for i in range(k, n):
            # Update sliding window sum of length k ending at index i
            current_sum += arr[i] - arr[i - k]
            
            # Option 1: Just the window of size k
            # Option 2: Extend the window to the left using the optimal previous prefix from Kadane's
            max_result = max(max_result, current_sum, current_sum + max_sum[i - k])
            
        return max_result