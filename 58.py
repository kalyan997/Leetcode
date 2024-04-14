class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.rstrip()
        n = len(s)
        res = 0
        
        #print(s)
        #print(n)
        for i in range(n-1, -1, -1):
            #print(i)
            if s[i] == " ":
                break
            res += 1
            
        return res