class Solution:
    def reducePairs(self, arr):
        stack = []
        for num in arr:
            while stack and (stack[-1] * num < 0):  # opposite signs
                if abs(stack[-1]) > abs(num):
                    num = stack[-1]  # keep bigger abs value
                elif abs(stack[-1]) < abs(num):
                    # keep num, discard stack[-1]
                    pass
                else:
                    num = None  # equal abs → remove both
                stack.pop()
                if num is None:
                    break
            if num is not None:
                stack.append(num)
        return stack