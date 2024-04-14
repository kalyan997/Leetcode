class Solution:
    def hammingWeight(self, n: int) -> int:
        num_bits = 0
        mask = 1
        for i in range(32):
            if n&mask != 0:
                num_bits+=1
            mask = mask<<1
        return num_bits