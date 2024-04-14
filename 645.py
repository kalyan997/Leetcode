class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        my_set = set()
        res = []
        
        for num in nums:
            if num in my_set:
                res.append(num)
            else:
                my_set.add(num)
        
        for i in range(1,len(nums)+1):
            if i not in my_set:
                res.append(i)
                return res