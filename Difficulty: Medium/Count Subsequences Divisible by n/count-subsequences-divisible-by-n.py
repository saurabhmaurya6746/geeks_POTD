class Solution:
    def countSubsequences(self, s, n):
        # code here
 
            MOD = 10**9 + 7

            # dp[r] = number of subsequences with remainder r
            dp = [0] * n
            dp[0] = 1  # empty subsequence

            for ch in s:
                digit = int(ch)
                new_dp = dp[:]  # copy current state (not including current digit)

                # Include current digit
                for r in range(n):
                    if dp[r] > 0:
                        new_r = (r * 10 + digit) % n
                        new_dp[new_r] = (new_dp[new_r] + dp[r]) % MOD

                dp = new_dp

            # Subtract the empty subsequence
            return (dp[0] - 1) % MOD
 