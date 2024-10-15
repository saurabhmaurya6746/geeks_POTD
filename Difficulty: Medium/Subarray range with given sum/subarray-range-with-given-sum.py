#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
   
        mp = dict()
        s = ans = 0
        mp[0] = 1
        
        for element in arr:
            s += element
            
            if s - tar in mp:
                ans += mp[s-tar]
            
            if s in mp:
                mp[s] += 1
            else:
                mp[s] = 1
        
        return ans
        #Your code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends