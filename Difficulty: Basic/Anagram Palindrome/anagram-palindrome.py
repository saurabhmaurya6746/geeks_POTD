class Solution:
    def canFormPalindrome(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        odd_count = sum(1 for v in freq.values() if v % 2 != 0)
        return odd_count <= 1