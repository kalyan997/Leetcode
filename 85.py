class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        R = len(matrix)
        C = len(matrix[0])
        
        columns = [[0]*(C+1) for _ in range(R+1)]
        
        for x in range(R):
            for y in range(C):
                columns[x+1][y] = columns[x][y] + int(matrix[x][y])
            
        def all_ones(top, bot, y):
            return columns[bot+1][y] - columns[top][y] == bot-top+1
        
        best = 0
        for top in range(R):
            for bot in range(top, R):
                current = 0
                
                for y in range(C):
                    if all_ones(top, bot, y):
                        current += 1
                    else:
                        current = 0
                    
                    best = max(best, current*(bot-top+1))
                    
        return best