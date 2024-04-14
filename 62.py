class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        visited = set()
        grid = [[0]*n for i in range(m)]
        my_q = deque()

        my_q.append([0,0])
        visited.add((0,0))

        def isValidCoor(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return False
            return True
        
        grid[0][0] = 1
        directions = [[1,0],[0,1]]
        while my_q:
            curr = my_q.popleft()
            curr_i, curr_j = curr[0], curr[1]
            
            for direction in directions:
                next_i, next_j = curr_i + direction[0], curr_j + direction[1]
                if isValidCoor(next_i, next_j):
                    grid[next_i][next_j] += grid[curr_i][curr_j]
                if isValidCoor(next_i, next_j) and (next_i, next_j) not in visited:
                    my_q.append([next_i,next_j])
                    visited.add((next_i,next_j))
        return grid[m-1][n-1]