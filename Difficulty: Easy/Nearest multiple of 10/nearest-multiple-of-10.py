#User function Template for python3

class Solution:
     
    def roundToNearest(self, num_str: str) -> str:
        # Get the length of the string
        n = len(num_str)
        
        # If the last digit is less than or equal to 5, round down
        if num_str[n-1] <= '5':
            num_str = num_str[:-1] + '0'
            return num_str
        
        # If the last digit is greater than 5, round up
        num_str = num_str[:-1] + '0'
        i = n - 2
        
        # Traverse backwards to handle cases like '99', '999', etc.
        while i >= 0 and num_str[i] == '9':
            num_str = num_str[:i] + '0' + num_str[i+1:]
            i -= 1
        
        # If all digits were '9', prepend '1'
        if i < 0:
            num_str = '1' + num_str
        else:
            # Increment the digit at index i
            num_str = num_str[:i] + chr(ord(num_str[i]) + 1) + num_str[i+1:]
        
        return num_str

 

#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends