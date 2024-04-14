class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = []
        
        for num in nums:
            if nums[abs(num)-1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] = -1 * nums[abs(num)-1]
                
        return res[0]
            