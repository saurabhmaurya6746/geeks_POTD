class Solution:
    def mergeArrays(self, a, b):
        i = len(a) - 1
        j = 0

        # Compare elements from the end of `a` and the start of `b`
        while i >= 0 and j < len(b):
            if a[i] < b[j]:
                break
            else:
                a[i], b[j] = b[j], a[i]  # Swap elements
                i -= 1
                j += 1

        # Sort both arrays
        a.sort()
        b.sort()

        return
        # code here


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends