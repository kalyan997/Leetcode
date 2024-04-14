class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        mask = 1
        for i in range(32):
            curr_bit = n%2
            res = (res<<1)+curr_bit
            n = n//2
        return res