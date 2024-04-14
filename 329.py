class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        def isValidCoor(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            return True

        indegree = [[0] * n for _ in range(m)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(m):
            for j in range(n):
                for dir in directions:
                    nxt_row, nxt_col = i + dir[0], j + dir[1]
                    if isValidCoor(nxt_row, nxt_col) and matrix[nxt_row][nxt_col] > matrix[i][j]:
                        indegree[nxt_row][nxt_col] += 1
        #print(indegree)
        my_q = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    my_q.append([i, j])
                    visited.add((i,j))

        ans = 0 
        
        #print(my_q)
        while my_q:
            ans += 1
            q_size = len(my_q)
            #print(my_q, len(my_q))
            for _ in range(q_size):
                curr_coor = my_q.popleft()
                c_row, c_col = curr_coor[0], curr_coor[1]
                for dir in directions:
                    nxt_row, nxt_col = c_row + dir[0], c_col + dir[1]
                    if isValidCoor(nxt_row, nxt_col) and (nxt_row,nxt_col) not in visited:
                        if matrix[nxt_row][nxt_col] > matrix[c_row][c_col]:
                            indegree[nxt_row][nxt_col] -= 1

                        if indegree[nxt_row][nxt_col] == 0:
                            my_q.append([nxt_row, nxt_col])
                            visited.add((nxt_row,nxt_col))
                #print(indegree)
        return ans