class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        s1, s2 = float("inf"), float("inf")
        
        for x in nums:
            print(s1, s2, x)
            if x > s2:
                return True
            if x > s1:
                s2 = min(x, s2)
            s1 = min(x, s1)
            
        return False