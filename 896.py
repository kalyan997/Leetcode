class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        increasing, decreasing = True, True
        for  i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                decreasing = False
            if nums[i] < nums[i+1]:
                increasing = False

        return decreasing or increasing