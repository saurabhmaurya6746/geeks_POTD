class Solution:
    def minProd(self, arr):
        n = len(arr)
    
        # If only one element
        if n == 1:
            return arr[0]
    
        # Count negative numbers and find other properties
        neg_count = 0
        zero_count = 0
        min_positive = float('inf')
        max_negative = float('-inf')  # negative number with smallest absolute value
    
        for num in arr:
            if num < 0:
                neg_count += 1
                max_negative = max(max_negative, num)
            elif num == 0:
                zero_count += 1
            else:  # num > 0
                min_positive = min(min_positive, num)
    
        # If there are zeros and no way to get negative product
        if zero_count > 0 and neg_count == 0:
            return 0
    
        # If there's an odd number of negatives, product of all non-zero elements is negative
        if neg_count % 2 == 1:
            product = 1
            for num in arr:
                if num != 0:
                    product *= num
            return product
    
        # If there's an even number of negatives (and at least one negative)
        if neg_count > 0:
            product = 1
            excluded = False
            for num in arr:
                if num != 0:
                    if num == max_negative and not excluded:
                        excluded = True  # exclude the negative with smallest absolute value
                    else:
                        product *= num
            return product
    
        # If all numbers are positive (no negatives, no zeros)
        return min_positive