class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        n = len(s)
        factors = []
        
        for i in range(1,n//2 + 1):
            if n%i == 0:
                factors.append(i)
                
        #print(factors)
        for curr_len in factors:
            curr_str = s[0:curr_len]
            curr_ind = curr_len
            
            while curr_ind < n:
                if curr_str != s[curr_ind:curr_ind+curr_len]:
                    break
                curr_ind = curr_ind+curr_len
            #print(curr_len, curr_ind)
            if curr_ind == n:
                return True
        
        return False