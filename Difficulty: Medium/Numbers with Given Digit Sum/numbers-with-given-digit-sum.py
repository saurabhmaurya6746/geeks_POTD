class Solution:
    def countWays(self, n: int, total_sum: int) -> int:
        # Maximum possible sum for n digits is n * 9
        if total_sum < 1 or total_sum > 9 * n:
            return -1
            
        # DP table/memoization dictionary
        memo = {}
        
        def solve(digits_left, current_sum):
            # Base Cases
            if current_sum < 0:
                return 0
            if digits_left == 0:
                return 1 if current_sum == 0 else 0
                
            # Check if already calculated
            state = (digits_left, current_sum)
            if state in memo:
                return memo[state]
                
            ans = 0
            # Agar yeh first digit hai (i.e., digits_left == n), toh range 1 to 9 hogi.
            # Baaki positions ke liye range 0 to 9 hogi.
            start_digit = 1 if digits_left == n else 0
            
            for digit in range(start_digit, 10):
                ans += solve(digits_left - 1, current_sum - digit)
                
            memo[state] = ans
            return ans

        result = solve(n, total_sum)
        
        # Agar koi bhi valid number nahi mila
        return result if result > 0 else -1