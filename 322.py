class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float("inf")] * (amount+1) for i in range(n+1)]
        #coins.sort()
        
        for i in range(0,len(coins)+1):
            dp[i][0] = 0
        for i, coin in enumerate(coins):
            curr_row = i+1
            for j in range(1,amount+1):
                if j<coin:
                    dp[curr_row][j] = dp[curr_row-1][j]
                    continue
                dp[curr_row][j] = min(dp[curr_row-1][j],dp[curr_row][j-coin]+1)
        #print(dp)
        return dp[n][amount] if dp[n][amount]!=float('inf') else -1