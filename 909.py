class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        grid = [0]*((n**2)+1)
        trav_grid = [[0]*n for i in range(n)]

        for i in range(n):
            for j in range(n):
                trav_grid[i][j] = board[n-1-i][j]

        for i in range(n):
            if i%2==1:
                left, right = 0, n-1
                while left<right:
                    trav_grid[i][left], trav_grid[i][right] = trav_grid[i][right], trav_grid[i][left]
                    left += 1
                    right -= 1

        directions = [1,2,3,4,5,6]
        res = 0
        curr_ind = 1
        
        for i in range(n):
            for j in range(n):
                grid[curr_ind] = trav_grid[i][j]
                curr_ind += 1
                
        my_q = deque()
        my_q.append([1,0])
        
        res_grid = [float('inf')]*((n**2)+1)
        visited = set()
        visited.add(1)
        res_grid[1] = 0

        while my_q:
            curr_size = len(my_q)
            
            for i in range(curr_size):
                curr = my_q.popleft()
                curr_index, curr_val = curr[0], curr[1]

                for direction in directions:
                    next_index = curr_index + direction
                    if next_index <= (n**2):
                        if grid[next_index] != -1:
                            next_index = grid[next_index]
                        res_grid[next_index] = min(res_grid[next_index], curr_val + 1)
                        if next_index not in visited:
                            my_q.append([next_index, res_grid[next_index]])
                            visited.add(next_index)

        return res_grid[-1] if n**2 in visited else -1