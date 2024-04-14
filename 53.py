class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n

        for i,num in enumerate(nums):
            dp[i] = max(num,num+dp[i-1])

        max_sum = float("-inf")
        for num in dp:
            max_sum = max(num,max_sum)
        return max_sum