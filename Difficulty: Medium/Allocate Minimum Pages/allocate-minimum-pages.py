class Solution:
    
    # Function to check if allocation is possible with max_pages limit
    def is_possible(self, arr, n, k, max_pages):
        students_required = 1
        current_sum = 0
        
        for pages in arr:
            # If a single book has more pages than max_pages, allocation is not possible
            if pages > max_pages:
                return False
            
            if current_sum + pages > max_pages:
                # Allocate to the next student
                students_required += 1
                current_sum = pages
                
                # If more students are required than available, allocation is not possible
                if students_required > k:
                    return False
            else:
                current_sum += pages
        
        return True

    # Function to find minimum number of pages
    def findPages(self, arr, k):
        n = len(arr)
        if n < k:  # Not enough books for each student
            return -1
        
        low, high = max(arr), sum(arr)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.is_possible(arr, n, k, mid):
                result = mid  # Try to minimize max pages
                high = mid - 1
            else:
                low = mid + 1
        
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
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends