class Solution:
    def maxLen(self, arr):
        # code here
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i] = -1
        
        sum_map = {}  # To store the first occurrence of each prefix sum
        max_len = 0
        prefix_sum = 0
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            if prefix_sum == 0:
                max_len = max(max_len, i + 1)
            
            if prefix_sum in sum_map:
                max_len = max(max_len, i - sum_map[prefix_sum])
            else:
                sum_map[prefix_sum] = i
        
        return max_len



#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends