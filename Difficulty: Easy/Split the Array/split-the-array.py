#User function Template for python3
class Solution:
	 
 
    def countgroup(self, arr):
        MOD = 10**9 + 7
        xr = 0
        n = len(arr)
        
        # Calculate the total XOR of the array
        for num in arr:
            xr ^= num
        
        # If total XOR is not zero, no valid split exists
        if xr != 0:
            return 0
        
        # Calculate 2^(n-1) % MOD
        ans = 1
        for i in range(n - 1):
            ans = (ans * 2) % MOD
        
        # Return result after subtracting 1 (to exclude the empty subset case)
        return ans - 1



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends