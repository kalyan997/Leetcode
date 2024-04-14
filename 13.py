class Solution:
    
    def romanToInt(self, s: str) -> int:
        romans = ['I', 'V', 'X', 'L', 'C', 'D','M']
        intvalue = 0
        for i in range(0,len(s)-1):
            if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                intvalue = intvalue - 1
            elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                intvalue = intvalue - 10
            elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                intvalue = intvalue - 100
                
            elif s[i] == 'I' and (s[i+1] != 'V' and s[i+1] != 'X'):
                intvalue = intvalue + 1
            elif s[i] == 'X' and (s[i+1] != 'L' and s[i+1] != 'C'):
                intvalue = intvalue + 10
            elif s[i] == 'C' and (s[i+1] != 'D' and s[i+1] != 'M'):
                intvalue = intvalue + 100
                
            elif s[i] == 'V':
                intvalue = intvalue + 5
            elif s[i] == 'L':
                intvalue = intvalue + 50
            elif s[i] == 'D':
                intvalue = intvalue + 500
            else:
                intvalue = intvalue + 1000
                
        if s[len(s)-1] == 'I':
                intvalue = intvalue + 1
        elif s[len(s)-1] == 'X':
            intvalue = intvalue + 10
        elif s[len(s)-1] == 'C':
            intvalue = intvalue + 100

        elif s[len(s)-1] == 'V':
            intvalue = intvalue + 5
        elif s[len(s)-1] == 'L':
            intvalue = intvalue + 50
        elif s[len(s)-1] == 'D':
            intvalue = intvalue + 500
        else:
            intvalue = intvalue + 1000
        
        return intvalue
            
                
            
            
        