# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        total_sum = sum(arr)
        left_sum = 0
    
        for i, value in enumerate(arr):
            # Calculate the right sum by subtracting the current value
            right_sum = total_sum - left_sum - value
    
            # Check if left_sum equals right_sum
            if left_sum == right_sum:
                return i
    
            # Update left_sum by adding the current value
            left_sum += value
    
        # If no equilibrium point is found, return -1
        return -1





#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends