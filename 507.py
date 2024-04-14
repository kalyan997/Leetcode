class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        total = 0
        if num == 1:
            return False
        for i in range(1,int(floor(sqrt(num)))+1):
            if num%i != 0:
                continue
            
            dividend = i
            divisor = num//i
            total = total + dividend + divisor
         
        return total == 2*num
        