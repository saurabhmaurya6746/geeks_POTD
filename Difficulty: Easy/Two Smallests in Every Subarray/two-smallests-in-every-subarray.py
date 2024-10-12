class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        maxi = -1
        
        # Iterate over the array, starting from the second element
        for i in range(1,len(arr)):
            
            # Calculate the sum of the current element and the previous element
            maxi = max(maxi, arr[i] + arr[i - 1])
        
        return maxi



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    t = int(data[0])
    lines = data[1:]

    for line in lines:
        s = list(map(int, line.strip().split()))
        solution = Solution()
        res = solution.pairWithMaxSum(s)
        print(res)

# } Driver Code Ends