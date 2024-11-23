#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        # code here
        n = len(arr)
        if n == 1:
            return 0
        
        # Sort the array
        arr.sort()
        
        # Initialize result as the initial max difference
        min_diff = arr[-1] - arr[0]
        
        # Traverse the array and adjust heights
        for i in range(n - 1):
            # Possible new minimum and maximum heights
            smallest = min(arr[0] + k, arr[i+1] - k)
            largest = max(arr[-1] - k, arr[i] + k)
            
            # Update min_diff
            min_diff = min(min_diff, largest - smallest)
        
        return min_diff



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends