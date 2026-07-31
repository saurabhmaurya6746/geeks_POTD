class Solution:
    def countSubsets(self, arr):
        MOD = 10**9 + 7
        
        # 10 primes up to 30
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        
        # Frequency array for elements in arr (since arr[i] <= 30)
        freq = [0] * 31
        for num in arr:
            freq[num] += 1
            
        # dp[mask] stores the number of valid subsets having prime factor combination represented by 'mask'
        dp = [0] * 1024
        dp[0] = 1  # Base case: empty subset
        
        for num in range(2, 31):
            if freq[num] == 0:
                continue
            
            # Check if 'num' is square-free and find its prime bitmask
            temp = num
            mask = 0
            is_square_free = True
            
            for i, p in enumerate(primes):
                if temp % p == 0:
                    count = 0
                    while temp % p == 0:
                        count += 1
                        temp //= p
                    if count > 1:
                        is_square_free = False
                        break
                    mask |= (1 << i)
            
            # If the number has repeated prime factors (e.g., 4, 8, 9, 12...), skip it
            if not is_square_free:
                continue
            
            # DP transitions (update backward to avoid using the same element multiple times)
            count_num = freq[num]
            for current_mask in range(1023, -1, -1):
                if (current_mask & mask) == 0:  # Disjoint prime factor sets
                    dp[current_mask | mask] = (dp[current_mask | mask] + dp[current_mask] * count_num) % MOD

        # Sum of subsets for all non-zero masks (at least one prime factor present)
        total_valid_subsets = sum(dp[1:]) % MOD
        
        # Multiply by 2^(count of 1s) because each '1' can either be included or excluded
        ones_factor = pow(2, freq[1], MOD)
        
        ans = (total_valid_subsets * ones_factor) % MOD
        return ans