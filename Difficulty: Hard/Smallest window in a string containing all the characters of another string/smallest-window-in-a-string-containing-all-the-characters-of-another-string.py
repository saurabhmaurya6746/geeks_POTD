#User function Template for python3


class Solution:
    
    def smallestWindow(self, s: str, p: str) -> str:
        min_len = float('inf')
        sind = -1
        r = 0
        l = 0
        mp = [0] * 256
        
        for char in p:
            mp[ord(char)] += 1
        
        cnt = 0
        
        while r < len(s):
            if mp[ord(s[r])] > 0:
                cnt += 1
            mp[ord(s[r])] -= 1
            
            while cnt == len(p):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    sind = l
                
                mp[ord(s[l])] += 1
                if mp[ord(s[l])] > 0:
                    cnt -= 1
                l += 1
                
            r += 1
        
        return "-1" if sind == -1 else s[sind:sind + min_len]


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

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends