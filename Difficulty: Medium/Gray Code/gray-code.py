class Solution:
    def graycode(self, n):
        res = []
        for i in range(1 << n):  # 0 to 2^n - 1
            gray = i ^ (i >> 1)  # formula for Gray code
            res.append(format(gray, '0{}b'.format(n)))  # binary string with leading zeros
        return res