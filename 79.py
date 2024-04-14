class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def isValidCoor(i, j):
            if i<0 or i>=rows or j<0 or j>=cols:
                return False
            return True
        
        def backtrack(i, j, visited, curr_ind):
            #print(i, j, curr_ind)
            if curr_ind >= len(word):
                return False
            
            if board[i][j] != word[curr_ind]:
                return False
            
            if curr_ind == len(word)-1:
                return True
            
            for direction in directions:
                next_row, next_col = i+direction[0], j+direction[1]
                
                if (next_row,next_col) not in visited and isValidCoor(next_row, next_col):
                    visited.add((next_row, next_col))
                    if backtrack(next_row, next_col, visited, curr_ind+1):
                        return True
                    visited.remove((next_row, next_col))
        
        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if backtrack(i, j, visited, 0):
                        return True
                    visited.remove((i, j))
                
                
        
        
        return False