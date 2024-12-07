class Solution:
    #User function Template for python3
     

    def merge(self, arr, low, high, mid):
        n1 = mid - low + 1
        n2 = high - mid

        # Creating temporary arrays
        arr1 = arr[low:low + n1]
        arr2 = arr[mid + 1:mid + 1 + n2]

        i = j = 0
        k = low

        # Merging while counting inversions
        while i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                j += 1
                self.ans += (n1 - i)
            k += 1

        # Copy remaining elements of arr1
        while i < n1:
            arr[k] = arr1[i]
            i += 1
            k += 1

        # Copy remaining elements of arr2
        while j < n2:
            arr[k] = arr2[j]
            j += 1
            k += 1

    def mergeSort(self, arr, low, high):
        if low >= high:
            return
        mid = low + (high - low) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.merge(arr, low, high, mid)

    def inversionCount(self, arr):
        self.ans = 0  # Reset the count
        self.mergeSort(arr, 0, len(arr) - 1)
        return self.ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends