class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp1_max = [0]*n
        dp2_min = [0]*n
        if len(nums)==1:
            return nums[0]
        dp1_max[0],dp2_min[0] = nums[0], nums[0]
        for i in range(1,n):
            if nums[i] == 0:
                continue
            dp1_max[i] = max(dp1_max[i-1]*nums[i],dp2_min[i-1]*nums[i],nums[i])
            dp2_min[i] = min(dp1_max[i-1]*nums[i],dp2_min[i-1]*nums[i],nums[i])

        max_prod = 0
        print(dp1_max)
        print(dp2_min)
        for curr_prod in dp1_max:
            max_prod = max(curr_prod,max_prod)

        return max_prod