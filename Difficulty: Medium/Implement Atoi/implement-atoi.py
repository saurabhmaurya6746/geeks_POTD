#User function template for Python
class Solution:
    def myAtoi(self, s: str) -> int:
        # Initialize variables
        i = 0
        n = len(s)
        result = 0
        sign = 1

        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Check for a sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Read digits and form the number
        while i < n and s[i].isdigit():
            digit = int(s[i])  # Convert the character to an integer
            result = result * 10 + digit
            i += 1

        # Apply the sign
        result *= sign

        # Clamp the result to the range [-2^31, 2^31 - 1]
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends