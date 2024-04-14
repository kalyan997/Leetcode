class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        m, n = left, right
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i