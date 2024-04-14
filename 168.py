class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        res = ""
        
        while columnNumber > 0:
            curr = (columnNumber-1)%26
            
            res = chr(ord('A')+curr) + res
            columnNumber = (columnNumber-1)//26
            
        return res