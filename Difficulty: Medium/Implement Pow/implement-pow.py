#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3
class Solution:
    def power(self, b: float, e: int) -> float:
        if e == 0:
            return 1.0  # Base case: anything raised to 0 is 1
        if e < 0:
            b = 1 / b
            e = -e  # Convert negative exponent to positive
        
        result = 1.0
        while e:
            if e % 2 == 1:  # If exponent is odd, multiply by base
                result *= b
            b *= b  # Square the base
            e //= 2  # Halve the exponent
        
        return result

 
        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b = float(input())
        e = int(input())
        ob = Solution()
        result = ob.power(b, e)
        print(f"{result:.5f}")
        print("~")
# } Driver Code Ends