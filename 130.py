class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValidCoor(x,y):
            if x<0 or y<0 or x>=len(board) or y>=len(board[0]):
                return False
            return True

        def dfs(row, col):
            board[row][col] = "Y"
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dir in directions:
                next_row = row+dir[0]
                next_col = col+dir[1]
                if isValidCoor(next_row,next_col) and board[next_row][next_col]=="O":
                    dfs(next_row,next_col)
        
        for i in range(len(board[0])):
            if board[0][i] == "O":
                dfs(0, i)
            if board[len(board) - 1][i] == "O":
                dfs(len(board) - 1, i)

        for i in range(len(board)):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][len(board[0]) - 1] == "O":
                dfs(i, len(board[0]) - 1)
        
        print(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "Y":
                    board[i][j] = "O"
        print(board)