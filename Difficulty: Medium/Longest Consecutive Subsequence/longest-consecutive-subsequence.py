 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here\\
        num_set = set(arr)
        max_length = 0
    
        # Iterate over each element in the array
        for num in arr:
            # Check if it's the starting point of a sequence
            if num - 1 not in num_set:
                # Initialize current number and current length
                current_num = num
                current_length = 1
    
                # Check for the next consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
    
                # Update the maximum length
                max_length = max(max_length, current_length)
    
        return max_length



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends