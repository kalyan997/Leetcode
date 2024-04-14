class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        res = []
        
        if len(nums) == 0:
            return res
        start = nums[0]
        prev = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] != prev+1:
                res.append(str(start)+ "->" +str(prev))
                start = nums[i]
            prev = nums[i]
        res.append(str(start)+ "->" +str(prev))
        
        for i, curr in enumerate(res):
            start, end = curr.split("->")
            if start == end:
                res[i] = start
            
        return res