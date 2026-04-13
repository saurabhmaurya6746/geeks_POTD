class Solution:
    def nextPalindrome(self, num):
        n = len(num)

        # Special case: all 9's
        if all(d == 9 for d in num):
            return [1] + [0]*(n-1) + [1]

        mid = n // 2
        left = num[:mid]

        # Mirror left to right
        if n % 2:
            pal = left + [num[mid]] + left[::-1]
        else:
            pal = left + left[::-1]

        if pal > num:
            return pal

        # Increment the middle
        carry = 1
        if n % 2:
            num[mid] += carry
            carry = num[mid] // 10
            num[mid] %= 10
            left = num[:mid]
        else:
            left = num[:mid]

        i = mid - 1
        while carry and i >= 0:
            num[i] += carry
            carry = num[i] // 10
            num[i] %= 10
            i -= 1

        left = num[:mid]
        if n % 2:
            return left + [num[mid]] + left[::-1]
        else:
            return left + left[::-1]