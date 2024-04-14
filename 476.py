class Solution:
    def findComplement(self, num: int) -> int:
        
        res = 0
        curr_pos = 0
        while num>0:
            
            curr_bit = num%2
            num = num//2
            
            comp_bit = curr_bit^1
            if comp_bit == 1:
                res = 2**curr_pos + res
            curr_pos += 1
        return res
            
            