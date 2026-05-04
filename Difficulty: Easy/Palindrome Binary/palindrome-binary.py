class Solution:
    def isBinaryPalindrome(self, n):
        binary_str = bin(n)[2:]  # remove '0b' prefix
        return binary_str == binary_str[::-1]