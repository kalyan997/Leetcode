class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        Rows = m
        Cols = n
        maxMoves = maxMove
        MOD = 10**9 + 7
        
        dp = [[0]*Cols for _ in range(Rows)]
        
        for curr_move in range(maxMoves):
            temp = [[0]*Cols for _ in range(Rows)]
            for i in range(Rows):
                for j in range(Cols):
                    if i+1 == Rows:
                        temp[i][j] = (temp[i][j]+1)%MOD
                    else:
                        temp[i][j] = (temp[i][j]+dp[i+1][j])%MOD
                    if i-1 < 0:
                        temp[i][j] = (temp[i][j]+1)%MOD
                    else:
                        temp[i][j] = (temp[i][j]+dp[i-1][j])%MOD
                    if j+1 == Cols:
                        temp[i][j] = (temp[i][j]+1)%MOD
                    else:
                        temp[i][j] = (temp[i][j]+dp[i][j+1])%MOD
                    if j-1 < 0:
                        temp[i][j] = (temp[i][j]+1)%MOD
                    else:
                        temp[i][j] = (temp[i][j]+dp[i][j-1])%MOD
            dp = temp
            
        return dp[startRow][startColumn]