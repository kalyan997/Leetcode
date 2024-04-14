class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set()
        for word in wordDict:
            words.add(word)
        n = len(s)
        if n == 0:
            return true
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(0,n):
            for j in range(-1,i):
                if dp[j+1]== True and (s[j+1:i+1] in words):
                    dp[i+1] = True 
        print(dp)
        return dp[n]     