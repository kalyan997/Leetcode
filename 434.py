class Solution:
    def countSegments(self, s: str) -> int:
        res = 0
        prev = False
        for i in range(len(s)):
            if s[i] != " " and prev == False:
                res += 1
                prev = True
            elif s[i] == " ":
                prev = False
        return res