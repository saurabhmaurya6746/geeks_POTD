class Solution:
    # Function to find the majority elements in the array
 
    def findMajority(self, nums):
        # Initialize variables
        ele1, ele2 = None, None
        count1, count2 = 0, 0
        n = len(nums)
        
        # Step to find potential candidates
        for num in nums:
            if ele1 == num:
                count1 += 1
            elif ele2 == num:
                count2 += 1
            elif count1 == 0:
                ele1 = num
                count1 = 1
            elif count2 == 0:
                ele2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step to check if the candidates are actual majorities
        freq1, freq2 = 0, 0
        ans = []
        for num in nums:
            if num == ele1:
                freq1 += 1
            elif num == ele2:
                freq2 += 1
        
        if freq1 > n // 3:
            ans.append(ele1)
        if freq2 > n // 3:
            ans.append(ele2)
        
        if len(ans) == 0:
            return [-1]
        
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends