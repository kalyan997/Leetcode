class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        
        if num == 0:
            return "0"
        
        neg = False
        if num < 0:
            neg = True
            num = (-1)*num
        while num > 0:
            #print(num)
            rem = num%7
            num = num//7
            res = str(rem) + res
            
        return res if neg==False else "-"+res