
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        my_list = [[0 for x in range(n)] for x in range(n)] 
        for i in range(n):
                my_list[i][i] = 1
      
        for ln in range(2,n+1):
            for i in range(n-ln+1):
                j = i + ln -1
                if s[i] == s[j] and ln == 2: 
                    my_list[i][j] = 2
                elif s[i] == s[j]:
                    my_list[i][j] = my_list[i+1][j-1] + 2
                else:
                    my_list[i][j] = max(my_list[i][j-1],my_list[i+1][j])

        return my_list[0][n-1]
        
        
    