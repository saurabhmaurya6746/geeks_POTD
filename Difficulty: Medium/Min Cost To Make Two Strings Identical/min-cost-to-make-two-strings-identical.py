class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        m, n = len(s1), len(s2)

        # DP table to find LCS length
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        lcs_length = dp[m][n]

        # Calculate minimum cost
        cost = (m - lcs_length) * costS1 + (n - lcs_length) * costS2

        return cost