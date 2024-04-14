class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==1:
            return 1
        
        prev = 2
        prev_2 = 1
        
        for i in range(2,n):
            curr = prev+prev_2
            prev_2 = prev
            prev = curr
        
        return prev