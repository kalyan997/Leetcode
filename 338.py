class Solution:
    def countBits(self, n: int) -> List[int]:
        num_1_bits = [0]*(n+1)
        
        for i in range(1,n+1):
            if i%2 == 0:
                num_1_bits[i] = num_1_bits[i//2]
            else:
                num_1_bits[i] = num_1_bits[i//2]+1
        return num_1_bits