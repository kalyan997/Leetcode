class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[first_zero] = nums[first_zero], nums[i]
                first_zero += 1
        return nums