class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_t = 0

        for num in nums:
            xor_t = xor_t^num
        return xor_t