#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        
        intervals.sort(key=lambda x: x[1])
    
        # Initialize variables
        prev_end = float('-inf')  # Initially, no interval selected
        remove_count = 0
        
        # Iterate through sorted intervals
        for start, end in intervals:
            if start < prev_end:  # Overlapping
                remove_count += 1
            else:
                prev_end = end  # Update the end of the current non-overlapping interval
        
        return remove_count

        
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends