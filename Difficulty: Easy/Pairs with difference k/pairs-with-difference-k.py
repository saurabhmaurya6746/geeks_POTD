#User function Template for python3
class Solution:
    def countPairsWithDiffK(self, arr, k):
        n = len(arr)
        maxi = max(arr)  # Find the maximum value in the array
        
        # Create a count array to store frequency of each element
        count = [0] * (maxi + 1)
        
        # Count the frequency of each element in arr
        for num in arr:
            count[num] += 1
        
        ans = 0
        for i in range(maxi + 1):
            if count[i] > 0:
                # If k == 0, count pairs of the same number
                if k == 0:
                    ans += count[i] * (count[i] - 1) // 2
                # If k > 0, count pairs with difference k
                elif i + k <= maxi:
                    ans += count[i] * count[i + k]
        
        return ans
 




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends