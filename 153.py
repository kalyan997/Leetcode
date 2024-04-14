class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<high:
            mid = int(low +(high-low)/2)
            if nums[low]>nums[mid]:
                high = mid
            elif nums[mid]>nums[high]:
                low = mid+1
            else:
                break
        return nums[low]