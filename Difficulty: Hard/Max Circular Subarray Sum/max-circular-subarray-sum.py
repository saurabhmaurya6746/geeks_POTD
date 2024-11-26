#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    def kadane(nums):
        max_ending_here = max_so_far = nums[0]
        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Step 1: Find the maximum subarray sum using Kadane's algorithm
    max_kadane = kadane(arr)
    
    # Step 2: Find the maximum circular subarray sum
    total_sum = sum(arr)
    # Invert the elements to find the minimum subarray sum
    inverted_sum = kadane([-x for x in arr])
    max_circular = total_sum + inverted_sum  # Total sum - minimum subarray sum

    # Step 3: Return the maximum of the two cases
    # Edge case: if all numbers are negative
    if max_circular == 0:
        return max_kadane
    return max(max_kadane, max_circular)
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends