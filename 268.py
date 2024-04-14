class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        xor_val = 0
        for num in nums:
            xor_val = xor_val^num

        for i in range(len(nums)+1):
            xor_val = xor_val^i
        return xor_val