class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        start = 0
        end = len(s)-1
        res = ""
        while start <= end:
            curr_end = min(start+k-1,end)
            res += "".join(reversed(s[start:curr_end+1]))
            res += s[curr_end+1:min(curr_end+k+1,end+1)]
            start += 2*k
        return res