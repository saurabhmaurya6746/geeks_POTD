#User function Template for python3

class Solution:
    def solveSudoku(self, mat):
        self.solve(mat)
    
    def solve(self, board):
        empty = self.findEmpty(board)
        if not empty:
            return True  # If there's no empty cell, the Sudoku is solved
        row, col = empty
        
        for num in range(1, 10):  # Try numbers from 1 to 9
            if self.isValid(board, row, col, num):
                board[row][col] = num
                if self.solve(board):
                    return True
                board[row][col] = 0  # Backtrack if placing num doesn't lead to a solution
        
        return False  # Trigger backtracking
    
    def findEmpty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)  # Return first empty cell
        return None
    
    def isValid(self, board, row, col, num):
        # Check row and column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        # Check 3x3 grid
        startRow, startCol = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == num:
                    return False
        
        return True
    
    def nQueen(self, n):
        def solve(col, diagonals, antiDiagonals, rows, board, res):
            if col == n:
                res.append(board[:])
                return
            
            for row in range(1, n + 1):
                if row in rows or (col - row) in diagonals or (col + row) in antiDiagonals:
                    continue
                
                rows.add(row)
                diagonals.add(col - row)
                antiDiagonals.add(col + row)
                board.append(row)
                
                solve(col + 1, diagonals, antiDiagonals, rows, board, res)
                
                rows.remove(row)
                diagonals.remove(col - row)
                antiDiagonals.remove(col + row)
                board.pop()
        
        res = []
        solve(0, set(), set(), set(), [], res)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        matrix = []
        n = 9
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.solveSudoku(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends