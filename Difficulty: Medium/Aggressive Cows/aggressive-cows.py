#User function Template for python3


class Solution:
    def aggressiveCows(self, stalls, k):
        def is_feasible(stalls, k, mid):
            # Check if we can place `k` cows with at least `mid` distance apart
            count = 1  # Place the first cow in the first stall
            last_position = stalls[0]
            
            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= mid:
                    count += 1
                    last_position = stalls[i]
                    if count == k:  # All cows placed successfully
                        return True
            return False

        stalls.sort()  # Sort the stalls
        low, high = 1, stalls[-1] - stalls[0]  # Minimum and maximum possible distances
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            if is_feasible(stalls, k, mid):
                result = mid  # Update result and search for larger distances
                low = mid + 1
            else:
                high = mid - 1
        
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends