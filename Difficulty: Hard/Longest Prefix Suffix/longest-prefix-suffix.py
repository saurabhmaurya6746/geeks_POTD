#User function Template for python3

class Solution:
	def lps(self, s: str) -> int:
        # Codegenius
        n = len(s)
        p, s_idx, pos, count = 0, 1, 1, 0
        
        while p < n and s_idx < n:
            if s[p] == s[s_idx]:
                p += 1
                s_idx += 1
                count += 1
            else:
                p = 0
                pos += 1
                s_idx = pos
                count = 0
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.lps(s)
        print(answer)

# } Driver Code Ends