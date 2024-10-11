#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    def rearrange(self, arr):
        n = len(arr)
        result = [-1] * n  # Initialize result array with -1
        
        # Place each element at its correct position
        for i in range(n):
            if arr[i] != -1 and arr[i] < n:
                result[arr[i]] = arr[i]
        
        return result
        #Code here

#{ 
 # Driver Code Starts.
def main():
    t = int(input())
    for _ in range(t):
        input_str = input()
        arr = list(map(int, input_str.split()))
        solution = Solution()
        ans = solution.rearrange(arr)
        print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
# } Driver Code Ends