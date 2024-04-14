class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            return 0
        left = 0
        prod = 1
        
        res = 0
        for right in range(len(nums)):
            prod = prod * nums[right]
            
            while prod >= k:
                prod = prod//nums[left]
                left += 1
            res = res + (right-left+1)
            
        return res