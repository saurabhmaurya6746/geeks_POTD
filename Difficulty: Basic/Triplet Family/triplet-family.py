class Solution:
    def findTriplet(self, arr):
        for i in range(len(arr)):
            target = arr[i]
            # Create a set to store complements for the target sum
            seen = set()
            
            # Check if any two elements in arr sum to target
            for j in range(len(arr)):
                if i != j:  # Ensure we don't use the same element twice
                    complement = target - arr[j]
                    
                    # If complement exists in seen set, we found a triplet
                    if complement in seen:
                        return True
                    # Add current element to the seen set
                    seen.add(arr[j])
                    
        # If no such triplet exists, return False
        return False
    

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends