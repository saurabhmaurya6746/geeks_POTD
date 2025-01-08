#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        n = len(arr)
        if n < 3:
            return 0  # Not enough sides to form a triangle
        
        # Sort the array
        arr.sort()
        count = 0
        
        # Fix the largest side
        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                # Check if arr[i] + arr[j] > arr[k]
                if arr[i] + arr[j] > arr[k]:
                    # All pairs (i, i+1, ..., j-1) with j are valid
                    count += (j - i)
                    j -= 1  # Decrease the second pointer
                else:
                    i += 1  # Increase the first pointer
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends