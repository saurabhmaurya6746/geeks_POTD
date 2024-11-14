#User function Template for python3

import heapq

class Solution:
    def nearlySorted(self, arr, k):
        # Initialize a min-heap with the first k+1 elements
        heap = arr[:k + 1]
        heapq.heapify(heap)
        
        index = 0
        
        # Process the elements from k+1 to the end of the array
        for i in range(k + 1, len(arr)):
            # Replace the element at 'index' with the smallest element from the heap
            arr[index] = heapq.heappop(heap)
            heapq.heappush(heap, arr[i])
            index += 1

        # Place remaining elements from the heap into the array
        while heap:
            arr[index] = heapq.heappop(heap)
            index += 1
        
        return arr  # Return the sorted array for convenience

# 

#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        # print("~")
        t -= 1
# } Driver Code Ends