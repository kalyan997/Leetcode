class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        my_map = {}
        left = 0
        for right in range(len(s)):
            if s[right] in my_map:
                left = max(left,my_map[s[right]])
            my_map[s[right]] = right+1
            res = max(res,right-left+1)
        return res