class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.rob_1(nums[:len(nums)-1]),self.rob_1(nums[1:]))

    def rob_1(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)
        def house_robber(nums,end):
            if end < 0:
                return 0
            if end == 0:
                memo[end] = nums[end]
            if end == 1:
                memo[end] = max(nums[end],nums[end-1])
            
            memo[end] = max(house_robber(nums,end-1),house_robber(nums,end-2)+nums[end])
            return memo[end]
        return house_robber(nums,len(nums)-1)