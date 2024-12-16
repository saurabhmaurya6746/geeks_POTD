#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        n1, n2 = len(a), len(b)
        merged_array = []
        i, j = 0, 0
    
        # Merge elements from both arrays
        while i < n1 and j < n2:
            if a[i] <= b[j]:
                merged_array.append(a[i])
                i += 1
            else:
                merged_array.append(b[j])
                j += 1
    
        # Add remaining elements from a (if any)
        while i < n1:
            merged_array.append(a[i])
            i += 1
    
        # Add remaining elements from b (if any)
        while j < n2:
            merged_array.append(b[j])
            j += 1
    
        return merged_array[k-1]

        # return c[k]
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends