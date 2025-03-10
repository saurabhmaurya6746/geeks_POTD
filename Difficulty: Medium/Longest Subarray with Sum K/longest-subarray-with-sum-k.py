# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_sum_map = {}
        prefix_sum = 0
        max_length = 0
    
        for i in range(len(arr)):
            # Update the prefix sum
            prefix_sum += arr[i]
    
            # Check if the current prefix sum is equal to k
            if prefix_sum == k:
                max_length = i + 1  # Subarray starts from index 0
    
            # Check if there exists a prefix sum that matches the required sum
            if (prefix_sum - k) in prefix_sum_map:
                max_length = max(max_length, i - prefix_sum_map[prefix_sum - k])
    
            # Store the first occurrence of the prefix sum
            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i
    
        return max_length

    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends