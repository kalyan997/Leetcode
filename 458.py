class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
        if buckets == 1:
            return 0
        
        def can_be_done(pigs):
            states_per_pig = minutesToTest // minutesToDie 
            total_states = states_per_pig ** pigs
            return total_states >= buckets
        left = 1
        right = buckets

        while left<right:
            mid = left + (right-left)//2
            if can_be_done(mid):
                right = mid
            else:
                left = mid+1
        return left