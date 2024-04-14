class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left, right = 0, len(nums)-1
        squares = [0]*len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left])>abs(nums[right]):
                squares[i] = nums[left]**2
                left += 1
            else:
                squares[i] = nums[right]**2
                right -= 1
                
        return squares        