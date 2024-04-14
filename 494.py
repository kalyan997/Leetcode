class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        res = 0

        def backtrack(i,curr_sum):
            nonlocal res
            
            if i == n:
                if curr_sum == target:
                    res += 1
                return
            curr_sum += nums[i]
            backtrack(i + 1,curr_sum)
            curr_sum  = curr_sum - 2*nums[i]
            backtrack(i + 1,curr_sum)

        backtrack(0,0)
        return res