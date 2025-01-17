#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        # Create an output array to store the results
        res = [1] * n
        
        # Calculate the left products and store in res
        left = 1
        for i in range(n):
            res[i] = left
            left *= arr[i]
        
        # Calculate the right products and update res
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= arr[i]
        
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends