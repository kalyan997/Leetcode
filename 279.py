class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")]*(n+1)
        
        squares = set()
        
        #print(floor(sqrt(n)))
        for i in range(1,ceil(sqrt(n))+1):
            squares.add(i**2)
        #print(squares)
        
        dp[0] = 0
        for i in range(n+1):
            if i in squares:
                dp[i] = 1
            for curr in squares:
                if i-curr > 0:
                    dp[i] = min(dp[i],1+dp[i-curr])
        #print("dp:",dp)
        return dp[n]