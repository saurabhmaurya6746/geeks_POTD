
        # code here
class Solution:
    def myAtoi(self, s):
        s = s.lstrip()  # remove leading spaces
        if not s:
            return 0
        
        sign = 1
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                break
        
        num *= sign
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN
        return num