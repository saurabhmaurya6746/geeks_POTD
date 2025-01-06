#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # If there are less than 2 elements, no pair exists
        arr.sort()  # Sort the array
        left, right = 0, len(arr) - 1
        closest_pair = []
        closest_diff = float('inf')
        max_abs_diff = -1
    
        while left < right:
            current_sum = arr[left] + arr[right]
            current_diff = abs(current_sum - target)
            current_abs_diff = abs(arr[right] - arr[left])
    
            # Check if this pair is closer to the target, or if it's a tie with a greater abs difference
            if current_diff < closest_diff or (current_diff == closest_diff and current_abs_diff > max_abs_diff):
                closest_pair = [arr[left], arr[right]]
                closest_diff = current_diff
                max_abs_diff = current_abs_diff
    
            # Move pointers based on comparison
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                break  # Exact match found
    
        return closest_pair
    
     

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends