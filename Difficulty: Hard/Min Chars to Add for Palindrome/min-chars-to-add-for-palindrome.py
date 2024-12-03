class Solution:
    def minChar(self, s):
        def compute_lps(pattern):
            n = len(pattern)
            lps = [0] * n
            length = 0  # length of the previous longest prefix suffix
            for i in range(1, n):
                while length > 0 and pattern[i] != pattern[length]:
                    length = lps[length - 1]
                if pattern[i] == pattern[length]:
                    length += 1
                lps[i] = length
            return lps
    
        # Reverse the string and concatenate with separator
        rev_s = s[::-1]
        concat_s = s + "#" + rev_s
        
        # Compute LPS array
        lps = compute_lps(concat_s)
        
        # Calculate the minimum characters to add
        return len(s) - lps[-1]
        #Write your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends