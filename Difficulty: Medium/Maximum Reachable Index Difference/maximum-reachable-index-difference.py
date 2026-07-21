class Solution:
    def maxIndexDifference(self, s):
        n = len(s)
        
        # If no 'a' exists, return -1
        if 'a' not in s:
            return -1
        
        # dp[i] = maximum index we can reach starting from position i
        dp = [0] * n
        
        # best_end[char] = maximum dp value among all positions with this character
        best_end = {}
        
        # Process from right to left
        for i in range(n - 1, -1, -1):
            ch = s[i]
            
            # We can always stop at current position
            dp[i] = i
            
            # Try to jump to the next character
            next_char = chr(ord(ch) + 1)
            if next_char in best_end:
                # We can jump to some occurrence of next_char
                # and from there reach best_end[next_char]
                dp[i] = max(dp[i], best_end[next_char])
            
            # Update best_end for current character
            if ch not in best_end:
                best_end[ch] = dp[i]
            else:
                best_end[ch] = max(best_end[ch], dp[i])
        
        # Find maximum difference
        ans = -1
        for i in range(n):
            if s[i] == 'a':
                ans = max(ans, dp[i] - i)
        
        return ans