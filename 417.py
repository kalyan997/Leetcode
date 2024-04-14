class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pacific_reachable = [[0]*len(heights[0]) for row in range(len(heights))]
        atlantic_reachable = [[0]*len(heights[0]) for row in range(len(heights))]

        def isValidCoor(i,j):
            if i<0 or j<0 or i>=len(heights) or j>=len(heights[0]):
                return False
            return True

        for i in range(len(heights[0])):
            pacific_reachable[0][i] = 1
            atlantic_reachable[len(heights)-1][i] = 1

        for i in range(len(heights)):
            pacific_reachable[i][0] = 1
            atlantic_reachable[i][len(heights[0])-1] = 1
        
        def pacific_dfs(curr_row, curr_col):
            pacific_reachable[curr_row][curr_col] = 1
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dir in directions:
                next_row = curr_row+dir[0]
                next_col = curr_col+dir[1]
                if isValidCoor(next_row,next_col) and heights[next_row][next_col]>=heights[curr_row][curr_col] and pacific_reachable[next_row][next_col] != 1:
                    pacific_dfs(next_row,next_col)

        def atlantic_dfs(curr_row, curr_col):
            atlantic_reachable[curr_row][curr_col] = 1
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dir in directions:
                next_row = curr_row+dir[0]
                next_col = curr_col+dir[1]
                if isValidCoor(next_row,next_col) and heights[next_row][next_col]>=heights[curr_row][curr_col] and atlantic_reachable[next_row][next_col] != 1:
                    atlantic_dfs(next_row,next_col)
        

        for i in range(len(heights[0])):
            pacific_dfs(0,i)
            atlantic_dfs(len(heights)-1,i)

        for i in range(len(heights)):
            pacific_dfs(i,0)
            atlantic_dfs(i,len(heights[0])-1)
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific_reachable[i][j]==1 and atlantic_reachable[i][j]==1:
                    res.append([i,j])
        return res