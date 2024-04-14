class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_ind = 0
        max_reachable = 0
        for i, num in enumerate(nums):
            if max_reachable>=i:
                max_reachable = max(num+i,max_reachable)
        return max_reachable>=len(nums)-1