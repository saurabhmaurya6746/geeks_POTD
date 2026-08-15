from functools import lru_cache

class Solution:
    def countWithout(self, n: int, d: int) -> int:
        if n <= 0:
            return 0
        
        s = str(n)
        
        @lru_cache(None)
        def dp(idx: int, tight: bool, started: bool) -> int:
            if idx == len(s):
                return 1 if started else 0
            
            limit = int(s[idx]) if tight else 9
            count = 0
            
            for digit in range(limit + 1):
                new_tight = tight and (digit == limit)
                
                if not started:
                    if digit == 0:
                        # Abhi bhi leading zero chal raha hai
                        count += dp(idx + 1, new_tight, False)
                    else:
                        # Number yahan se start ho raha hai
                        if digit != d:
                            count += dp(idx + 1, new_tight, True)
                else:
                    # Number already start ho chuka hai, digit d allowed nahi hai
                    if digit != d:
                        count += dp(idx + 1, new_tight, True)
            
            return count

        return dp(0, True, False)