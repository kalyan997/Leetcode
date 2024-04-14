class Solution:
    def addDigits(self, num: int) -> int:
        
        curr = num
        
        def get_sum_digits(n):
            res = 0
            while n > 0:
                curr_digit = n%10
                res += curr_digit
                n = n//10
            return res
        
        while curr>9:
            curr = get_sum_digits(curr)
        
        return curr