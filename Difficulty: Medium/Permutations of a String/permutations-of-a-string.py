#User function Template for python3

class Solution:
    def findPermutation(self, s):
        def backtrack(start=0):
            # If we've generated a complete permutation, add it to the result
            if start == len(s):
                result.append("".join(s))
                return
            
            seen = set()  # To track duplicates at this level
            for i in range(start, len(s)):
                if s[i] in seen:
                    continue  # Skip duplicates
                seen.add(s[i])  # Mark this character as used
                
                s[start], s[i] = s[i], s[start]  # Swap characters
                backtrack(start + 1)  # Generate permutations for the rest
                s[start], s[i] = s[i], s[start]  # Undo the swap (backtrack)

        result = []
        s = sorted(list(s))  # Sort the string to handle duplicates properly
        backtrack()  # Start generating permutations
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends