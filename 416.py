class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num
        if sum%2 == 1:
            return False
        target = sum//2

        nums.sort()
        dp = [[False]*(target+1) for i in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = True
        for i,num in enumerate(nums):
            curr_row = i+1
            for j in range(1,target+1):
                if j<num:
                    dp[curr_row][j] = dp[curr_row-1][j]
                else:
                    dp[curr_row][j] = dp[curr_row-1][j] or dp[curr_row-1][j-num]

        return dp[len(nums)][target]