class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for i in range(len(coins)+1)]

        for i in range(len(coins)+1):
            dp[i][0] = 1

        for i,coin in enumerate(coins):
            curr_row = i+1
            for j in range(1,amount+1):
                if j<coin:
                    dp[curr_row][j] = dp[curr_row-1][j]
                else:
                    dp[curr_row][j] = dp[curr_row-1][j] + dp[curr_row][j-coin]
        return dp[len(coins)][amount]