class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
    
        # Initialize two pointers
        left = 0          # Pointer for the smallest elements
        right = len(arr) - 1  # Pointer for the largest elements
        
        # Initialize result array
        result = []
        
        # Alternate picking largest and smallest elements
        while left <= right:
            if left != right:
                result.append(arr[right])   # Add largest element
                result.append(arr[left])    # Add smallest element
            else:
                result.append(arr[left])    # Add the last middle element if length is odd
            left += 1
            right -= 1
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends