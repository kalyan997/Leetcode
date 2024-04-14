class Solution:
    def countSubstrings(self, s: str) -> int:
        
        max_len = 0
        res = ""
        num_palindromes = 0
        
        for i in range(0,len(s)):
            left, right = i, i
            
            while left>=0 and right<len(s):
                if s[left] == s[right]:
                    num_palindromes+=1 
                    left -= 1
                    right += 1
                else:
                    break
                    
        for i in range(0,len(s)):
            left, right = i, i+1
            
            while left>=0 and right<len(s):
                if s[left] == s[right]:
                    num_palindromes+=1
                    left -= 1
                    right += 1
                else:
                    break
        return num_palindromes