class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        curr, pos = 0, 0

        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
    
        return nums

        