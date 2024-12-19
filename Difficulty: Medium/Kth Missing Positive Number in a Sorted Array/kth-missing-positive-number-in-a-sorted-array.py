#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        n = len(arr)
    
    # Binary search to find the position
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            missing_count = arr[mid] - (mid + 1)
            
            if missing_count < k:
                left = mid + 1
            else:
                right = mid - 1
        
        # At the end of binary search, left points to the smallest index
        # where missing_count >= k
        return left + k


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends