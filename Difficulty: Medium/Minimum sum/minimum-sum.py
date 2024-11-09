#User function Template for python3

class Solution:
    def minSum(self, arr):
        # code here
        arr.sort()
        
        # Initialize two numbers as empty strings
        n1, n2 = "", ""
        
        # Distribute digits alternately to n1 and n2
        for i in range(len(arr)):
            if i % 2 == 0:
                n1 += str(arr[i])
            else:
                n2 += str(arr[i])
        
        # Reverse n1 and n2 to prepare for addition from least significant digits
        n1, n2 = n1[::-1], n2[::-1]
        
        # Initialize the result and carry for addition
        ans = []
        carry = 0
        i, j = 0, 0
        
        # Perform addition on each digit from least significant to most significant
        while i < len(n1) or j < len(n2) or carry:
            sum_val = carry
            if i < len(n1):
                sum_val += int(n1[i])
                i += 1
            if j < len(n2):
                sum_val += int(n2[j])
                j += 1
            
            # Update carry and the sum digit
            carry = sum_val // 10
            ans.append(str(sum_val % 10))
        
        # Join the result and reverse it to get the correct order
        result = ''.join(ans[::-1])
        
        # Remove any leading zeroes and return the result
        return result.lstrip('0') or '0'
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends