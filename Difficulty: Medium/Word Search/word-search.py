class Solution:
    def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])
        
        def dfs(x, y, index):
            if index == len(word):
                return True  # Successfully matched all characters
            
            if x < 0 or x >= n or y < 0 or y >= m or mat[x][y] != word[index]:
                return False  # Out of bounds or mismatch
            
            temp = mat[x][y]
            mat[x][y] = '#'  # Mark the cell as visited
            
            # Explore in all 4 directions: up, down, left, right
            found = (dfs(x + 1, y, index + 1) or 
                     dfs(x - 1, y, index + 1) or 
                     dfs(x, y + 1, index + 1) or 
                     dfs(x, y - 1, index + 1))
            
            mat[x][y] = temp  # Backtrack
            
            return found
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0] and dfs(i, j, 0):  # Start DFS from matching first character
                    return True
        
        return False  # Word not found

# Example usage:
# mat = [['T', 'E', 'E'], 
#       ['S', 'G', 'K'], 
#       ['T', 'E', 'L']]
# word = "GEEK"

# sol = Solution()
# print(sol.isWordExist(mat, word))  # Output: True



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends