class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total_sum = sum(nums)
        prev_sum = 0
        
        for i, num in enumerate(nums):
            if prev_sum == total_sum - prev_sum - num:
                return i
            prev_sum += num
            
        return -1