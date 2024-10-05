#User function Template for python3

class Solution:
     
    def findSmallest(self, arr):
        ans = 1
        for i in range(len(arr)):
            if arr[i] > ans:
                return ans
            ans += arr[i]
        return ans

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findSmallest(arr)
        print(ans)


if __name__ == "__main__":
    main()

# } Driver Code Ends