#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
    
    # Create a new array by taking elements alternatively from the sorted array
        n = len(arr)
        arranged = []
        
        # Using two pointers, one starting from the beginning and one from the end
        left, right = 0, n - 1
        while left <= right:
            if left == right:
                arranged.append(arr[left])
            else:
                arranged.append(arr[left])
                arranged.append(arr[right])
            left += 1
            right -= 1
        
        # Calculate the sum of absolute differences in the arranged circular array
        max_sum = 0
        for i in range(n):
            max_sum += abs(arranged[i] - arranged[(i + 1) % n])
        
        return max_sum
                
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends