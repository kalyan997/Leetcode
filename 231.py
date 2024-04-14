class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        powers_of_two = set()
        
        curr = 1
        MAX_VAL = 2**31 - 1
        MIN_VAL = -(2**31)
        
        
        while curr < MAX_VAL:
            powers_of_two.add(curr)
            curr = curr*2
        return True if n in powers_of_two else False