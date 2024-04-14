class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_streak = 0
        
        curr_streak = 0
        for num in nums:
            if num == 1:
                curr_streak += 1
                max_streak = max(curr_streak,max_streak)
            else:
                curr_streak = 0
                
        return max_streak