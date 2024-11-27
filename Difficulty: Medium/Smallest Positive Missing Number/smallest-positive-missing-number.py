#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        n = len(arr)

    # Step 1: Segregate positive and non-positive numbers
        # Place all positive numbers at the beginning
        j = 0
        for i in range(n):
            if arr[i] > 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        
        # Step 2: Mark indices for positive numbers
        # Work only on the first j elements (positive numbers)
        for i in range(j):
            val = abs(arr[i])
            if val <= j:
                arr[val - 1] = -abs(arr[val - 1])  # Mark index as visited
        
        # Step 3: Find the first index with a positive value
        for i in range(j):
            if arr[i] > 0:
                return i + 1
    
        # If all indices are visited, return j + 1
        return j + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends