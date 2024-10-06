#User function Template for python3

class Solution:
     
    def DFS(self, i, j, grid):
        grid[i][j] = 0
        
        if (i - 1 >= 0 and grid[i-1][j] == 1):
            self.DFS(i-1, j, grid)
        
        if (i + 1 < len(grid) and grid[i+1][j] == 1):
            self.DFS(i+1, j, grid)
        
        if (j + 1 < len(grid[i]) and grid[i][j+1] == 1):
            self.DFS(i, j + 1, grid)
        
        if (j - 1 >= 0 and grid[i][j-1] == 1):
            self.DFS(i, j - 1, grid)
        
        if (i - 1 >= 0 and j + 1 < len(grid[i]) and grid[i-1][j+1] == 1):
            self.DFS(i-1, j+1, grid)
        
        if (i-1 >= 0 and j - 1 >= 0 and grid[i-1][j-1] == 1):
            self.DFS(i-1, j-1, grid)
        
        if (i + 1 < len(grid) and j - 1 >= 0 and grid[i+1][j-1] == 1):
            self.DFS(i+1, j-1, grid)
        
        if (i + 1 < len(grid) and j + 1 < len(grid[i]) and grid[i+1][j+1] == 1):
            self.DFS(i+1, j+1, grid)
            
    def numIslands(self, grid):
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.DFS(i, j, grid)
                    
                    ans += 1
        
        return ans
        # code here


#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))

# } Driver Code Ends