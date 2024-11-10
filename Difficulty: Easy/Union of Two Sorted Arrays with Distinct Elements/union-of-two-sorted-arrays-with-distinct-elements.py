#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        n, m = len(a), len(b)
        i, j = 0, 0
        union_result = []
    
        while i < n and j < m:
            # If both elements are equal, add only one to result
            if a[i] == b[j]:
                union_result.append(a[i])
                i += 1
                j += 1
            # If element in a is smaller, add it to result and move pointer in a
            elif a[i] < b[j]:
                union_result.append(a[i])
                i += 1
            # If element in b is smaller, add it to result and move pointer in b
            else:
                union_result.append(b[j])
                j += 1
    
        # Add remaining elements of a, if any
        while i < n:
            union_result.append(a[i])
            i += 1
    
        # Add remaining elements of b, if any
        while j < m:
            union_result.append(b[j])
            j += 1
    
        return union_result
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")
# } Driver Code Ends