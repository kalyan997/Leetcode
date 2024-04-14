class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        negDiags = set()
        posDiags = set()
        res = []
        board = [["."]*n for i in range(n)]

        def backtrack(row):
            if row == n:
                new_board = []
                for curr_row in board:
                    new_board.append("".join(curr_row))
                res.append(new_board)
                return
            for col in range(n):
                if (col in cols) or (row+col in posDiags) or (row-col in negDiags):
                    continue
                cols.add(col)
                posDiags.add(row+col)
                negDiags.add(row-col)
                board[row][col] = "Q"
                backtrack(row+1)
                cols.remove(col)
                posDiags.remove(row+col)
                negDiags.remove(row-col)
                board[row][col] = "."
            return
        backtrack(0)
        return res