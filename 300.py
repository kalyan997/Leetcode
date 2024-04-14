class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(n-1,-1,-1):
            curr_ind = i
            for j in range(curr_ind+1,n):
                if nums[j]>nums[curr_ind]:
                    dp[curr_ind] = max(dp[j]+1,dp[curr_ind])
        return max(dp)